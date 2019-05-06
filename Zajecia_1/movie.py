movie = input("Movie title: ")
grade_overall = int(input("Overall grade: "))
grade_costume = int(input("Costume grade: "))
grade_music = int(input("Music grade: "))
mean_value = (grade_overall+grade_costume+grade_music) / 3
print("You have rated the " + movie + ".")
print("Mean grade: " + str(mean_value))
