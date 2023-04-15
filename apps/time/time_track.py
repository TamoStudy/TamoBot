import discord
import time

from tools.tamolog import TamoLogger

FOCUS_ROOMS = [851513379503079524]
user_time = {}

class TimeTrack():
    @staticmethod
    def update_time_on_event(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
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

        # Event when leaving a focus room
        if member.id in user_time and before.channel is not None and before.channel.id in FOCUS_ROOMS and (after.channel is None or after.channel.id not in FOCUS_ROOMS):
            """
            Calculate the focus time, update database, and then remove the member id from the
            user_time dictionary as they are no longer in a focus room.
            """
            try:
                focused_time_of_member = round(time.time() - user_time[member.id])
                tamo_tokens_earned = focused_time_of_member // 144
                TamoLogger.log("INFO", str(member.name) + " left " + str(before.channel.name) + ". " + str(focused_time_of_member) + " seconds added to time, earning " + str(tamo_tokens_earned) + " Tamo tokens.")
                del user_time[member.id]

                # Update MySQL User Entry
                TimeTrack.update_user_time_and_tokens_entry_in_database(member.id, focused_time_of_member, tamo_tokens_earned)
            except KeyError as e:
                TamoLogger.log("ERROR", f"KeyError occurred when accessing user_time. Invalid Key: {e.args[0]}")
            except:
                TamoLogger.log("ERROR", "An unexpected error occurred inside of TimeTrack.update_time_on_event.")

    @staticmethod
    def update_time_on_call(interaction: discord.Interaction, user: discord.User):
        """
        Under the condition that the /stats command is called on a particular user
        (if no user is provided, the calling user a part of the interaction will be
        inferred), the time will update and tamo tokens will be awarded.

        Additionally, if the user is connected to the voice channel, their
        time will be reset.
        """
        # Initially sets the user id as the caller id
        user_id = interaction.user.id

        # If a member id is given (ex. /stats Firebal#0676), this id is set
        if user is not None:
            user_id = user.id

        # Check if user is in voice channel, if they are update info accordingly
        if user_id in user_time:
            # Update Time based on voice connection
            try:
                focused_time_of_member = round(time.time() - user_time[user_id])
                tamo_tokens_earned = focused_time_of_member // 144
                TamoLogger.log("INFO", "Updating stats for " + str(user_id) + ". " + str(focused_time_of_member) + " seconds added to time, earning " + str(tamo_tokens_earned) + " Tamo tokens.")
                user_time[user_id] = time.time()

                # Update MySQL User Entry
                TimeTrack.update_user_time_and_tokens_entry_in_database(user_id, focused_time_of_member, tamo_tokens_earned)
            except KeyError as e:
                TamoLogger.log("ERROR", f"KeyError occurred when accessing user_time. Invalid Key: {e.args[0]}")
            except:
                TamoLogger.log("ERROR", "An unexpected error occurred inside of TimeTrack.update_time_on_event.")

    @staticmethod
    def update_user_time_and_tokens_entry_in_database(user_id, focus_time, tokens):
        # TODO
        pass
