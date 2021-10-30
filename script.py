authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
author_last_names = []
for author in author_names:
  last_name = author.split()[1]
  author_last_names.append(last_name)
print(author_last_names)
