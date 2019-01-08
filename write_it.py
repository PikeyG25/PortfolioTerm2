print("Creating a text file with the write() method")
text_file = open("write_it.txt","w")
text_file.write("line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
test_file.close()

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt","w")
lines = ["scores1\n",
             "scores2\n",
             "scores3\n"]
text_file.writelines(lines)
text_file.close()
