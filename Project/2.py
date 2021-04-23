#Height of the Tallest Building
def tallest_building_height(lst):
	return str(20*sum('#' in h for h in lst))+'m'

print(tallest_building_height([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]))