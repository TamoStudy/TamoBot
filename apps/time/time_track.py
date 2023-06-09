import discord
import time
import traceback

from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger

SECONDS_FOR_TAMO_TOKEN = 300
FOCUS_ROOMS = [977235101249327114, 851513379503079524, 973214029893992529]
user_time = {}

class TimeTrack():
    def __init__(self, db: MySQLConnection):
        self.db = db
        TamoLogger.loga("INFO", "TimeTrack.__init__(db)", f"db successfully initialized in time_track: {db}")

    def start_up(self, guild: discord.Guild):
        try:
            voice_channels = guild.voice_channels
            TamoLogger.loga("INFO", "TimeTrack.start_up(guild)", f"Successfully obtained voice channels from guild {voice_channels}.")
        except Exception as e:
            TamoLogger.loga("ERROR", "TimeTrack.start_up(guild)", f"An unexpected error occurred when fetching voice channels from guild. {e}")

        for channel in voice_channels:
            if isinstance(channel, discord.VoiceChannel) and channel.id in FOCUS_ROOMS:
                members = channel.members
                for member in members:
                    TamoLogger.loga("INFO", "TimeTrack.start_up(guild)", f"{member.name} was in {channel.name} on bot startup. Starting time.")
                    user_time[member.id] = time.time()
                    self.db.create_user_requirements_if_dne(member.id)

    def handle_shutdown(self, guild: discord.Guild):
        voice_channels = guild.voice_channels
        TamoLogger.loga("INFO", "TimeTrack.start_up(guild)", f"Successfully obtained voice channels from guild {voice_channels}.")

        for channel in voice_channels:
            if isinstance(channel, discord.VoiceChannel) and channel.id in FOCUS_ROOMS:
                members = channel.members
                for member in members:
                    if member.id in user_time:

                        focused_time_of_member = round(time.time() - user_time[member.id])
                        tamo_tokens_earned = (focused_time_of_member // SECONDS_FOR_TAMO_TOKEN)

                        # Update MySQL User Entry
                        self.update_user_time_and_tokens_entry_in_database(member.id, focused_time_of_member, tamo_tokens_earned)
                        TamoLogger.loga("SUCCESS", "TimeTrack.handle_shutdown", f"Member {member.name} time saved {focused_time_of_member}, earned {tamo_tokens_earned} tokens.")

    def update_connected_users(self, guild: discord.Guild):
        voice_channels = guild.voice_channels
        TamoLogger.loga("INFO", "TimeTrack.update_connected_users(guild)", f"Successfully obtained voice channels from guild {voice_channels}.")

        for channel in voice_channels:
            if isinstance(channel, discord.VoiceChannel) and channel.id in FOCUS_ROOMS:
                members = channel.members
                for member in members:

                    # If the user is connected, they should be in user_time
                    if member.id in user_time:
                        focused_time_of_member = round(time.time() - user_time[member.id])

                        tamo_tokens_earned = focused_time_of_member // SECONDS_FOR_TAMO_TOKEN

                        # Resetting time
                        user_time[member.id] = time.time()

                        # Update MySQL User Entry
                        self.update_user_time_and_tokens_entry_in_database(member.id, focused_time_of_member, tamo_tokens_earned)

                        TamoLogger.loga("SUCCESS", "TimeTrack.handle_shutdown", f"Member {member.name} time saved {focused_time_of_member}, earned {tamo_tokens_earned} tokens.")

    def update_time_on_event(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        TamoLogger.log("INFO", f"Update Time Event Received in Time Track. Current user_time {user_time}")

        # Event when joining a focus room
        if member.id not in user_time and (before.channel is None or before.channel not in FOCUS_ROOMS) and (after.channel is not None and after.channel.id in FOCUS_ROOMS):
            """
            Store user_time entry matching <member_id, time> key value pair.
            If /stats is ran when user is inside of vc (dictionary entry exists for
            that member_id) then we want to recalculate focus time, update the dictionary,
            update database, and reset the current focus time in the room to 0.
            """
            TamoLogger.log("INFO",str(member.name) + " joined " + str(after.channel.name))
            user_time[member.id] = time.time()
            self.db.create_user_requirements_if_dne(member.id)

        # Event when leaving a focus room
        if member.id in user_time and before.channel is not None and before.channel.id in FOCUS_ROOMS and (after.channel is None or after.channel.id not in FOCUS_ROOMS):
            """
            Calculate the focus time, update database, and then remove the member id from the
            user_time dictionary as they are no longer in a focus room.
            """
            try:
                focused_time_of_member = round(time.time() - user_time[member.id])
                tamo_tokens_earned = (focused_time_of_member // SECONDS_FOR_TAMO_TOKEN)

                TamoLogger.loga("INFO", "TimeTrack.update_time_on_event", str(member.name) + " left " + str(before.channel.name) + ". " + str(focused_time_of_member) + " seconds added to time, earning " + str(tamo_tokens_earned) + " Tamo tokens.")
                del user_time[member.id]

                # Update MySQL User Entry
                self.update_user_time_and_tokens_entry_in_database(member.id, focused_time_of_member, tamo_tokens_earned)
            except KeyError as e:
                TamoLogger.log("ERROR", f"KeyError occurred when accessing user_time. Invalid Key: {e.args[0]}")
            except Exception as e:
                TamoLogger.log("ERROR", f"An unexpected error occurred inside of TimeTrack.update_time_on_event for {member.name}.")
                traceback.print_exc()

    def update_time_on_call(self, interaction: discord.Interaction, user: discord.User):
        """
        Under the condition that the /stats command is called on a particular user
        (if no user is provided, the calling user a part of the interaction will be
        inferred), the time will update and tamo tokens will be awarded.

        Additionally, if the user is connected to the voice channel, their
        time will be reset.
        """
        # Initially sets the user id as the caller id
        calling_user = interaction.user

        # If a member id is given (ex. /stats Firebal#0676), this id is set
        if user is not None:
            calling_user = user

        self.db.create_user_requirements_if_dne(calling_user.id)
        # Check if user is in voice channel, if they are update info accordingly
        if calling_user.id in user_time:
            # Update Time based on voice connection
            try:
                focused_time_of_member = round(time.time() - user_time[calling_user.id])

                tamo_tokens_earned = focused_time_of_member // SECONDS_FOR_TAMO_TOKEN

                # Resetting Time
                user_time[calling_user.id] = time.time()

                TamoLogger.loga("INFO", "TimeTrack.update_time_on_call", "Updating /stats for " + str(calling_user.id) + ". " + str(focused_time_of_member) + " seconds added to time, earning " + str(tamo_tokens_earned) + " Tamo tokens.")

                # Update MySQL User Entry
                self.update_user_time_and_tokens_entry_in_database(calling_user.id, focused_time_of_member, tamo_tokens_earned)
            except KeyError as e:
                TamoLogger.log("ERROR", f"KeyError occurred when accessing user_time. Invalid Key: {e.args[0]}")
            except:
                TamoLogger.log("ERROR", "An unexpected error occurred inside of TimeTrack.update_time_on_event.")

    def update_user_time_and_tokens_entry_in_database(self, user_id, focus_time, tokens):
        # Quality check: ensure user requirements exist
        self.db.create_user_requirements_if_dne(user_id)

        TamoLogger.log("INFO", f"Updating time and tokens for {user_id}")
        self.db.update_user_total_entry(user_id, focus_time, tokens)
        