sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski","Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

sports_team_rosters["Pittsburg Steelers"] = ["Ben Rothlisberger", "Antonio Brown"]
print(sports_team_rosters)

sports_team_rosters["New York Giants"] = ["Eli Manning"]
print(sports_team_rosters)


video_game_options = {}
# video_game_options = dict()

video_game_options["subtitles"] = True
video_game_options["difficult"] = "Medium"
video_game_options["volume"] = 7
print(video_game_options)

video_game_options["difficult"] = "Hard"
video_game_options["subtitles"] = False
print(video_game_options)


words = ["danger", "beware","danger"]
def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words(words))