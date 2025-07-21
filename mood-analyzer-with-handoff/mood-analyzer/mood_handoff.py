from connection import config
from agents import Agent, Runner

mood_analyzer_agent = Agent(
    name = "checker_agent",
    instructions = """
checks the user’s mood from their message (like “happy”, “sad”, etc.)
""")

activity_suggester_agent = Agent(
    name = "activity_suggester_agent",
    instructions = """
If mood is “sad” or “stressed”,suggests an activity.
For example:
    - sad → "Take a walk outside and listen to calming music."
    - stressed → "Try deep breathing exercises or take a short break."

"""
)

user_input = input("Enter your message: ")

#user_input must be passed with the keyword input because all positional arguments must come before keyword arguments.

mood_result = Runner.run_sync(
    mood_analyzer_agent,
    input=user_input,
    run_config=config
)

mood = mood_result.final_output.strip().lower()
print("Detected Mood:", mood)

# Step 2: Run Activity Suggester Agent (only if needed)
if mood in ["sad", "stressed"]:
    activity_result = Runner.run_sync(
        activity_suggester_agent,
        input=mood,
        run_config=config
    )
    print("Suggested Activity:", activity_result.final_output)
else:
    print("No activity suggestion needed. You're doing great!")