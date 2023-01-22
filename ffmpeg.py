import argparse
parser = argparse.ArgumentParser(description="Help write triming video code in ffmpeg command by giving text file.")
parser.add_argument("-file", "-f", help="input text file, including triming time.", type=str, default="trim.txt")
parser.add_argument("-text", "-t", help="input text, including triming time.", type=str, default="")
parser.add_argument("-input", "-i", help="input video file.", type=str, default="input.mp4")
parser.add_argument("-output", help="output video file.", type=str, default="output.mp4")
parser.add_argument("-mute", "-m", help="mute video.", action="store_true")
args = parser.parse_args()

#input = "input.mp4"
#output = "output.mp4"
#string = "0:0 1:0,speed=3 2:0 3:0"
input, string, output = args.input, args.text, args.output
if not string:
  try:
    f = open(args.file, "r", encoding="utf-8")
    string = f.read()
    f.close()
  except Exception as e:
    print(e)
    print("Use Default Settting.\n")
    string = "0:0 1:0,speed=3 2:0 3:0\n"
string = string.replace("\n", " ")
string = string.replace(", ", ",").replace(",  ", ",").replace(",   ", ",")
string = string.replace("= ", "=").replace(" = ", "=").replace(" =", "=")
while ("  " in string):
  string = string.replace("  ", " ")
arrays = string.split(" ")
for check_empty in range(0, len(arrays))[::-1]:
  if not arrays[check_empty]: arrays.pop(check_empty)
#print("Use setting:", arrays, "\n")
i = 0
iv = 0
ia = 0
video = ""
audio = ""
#all_mute = False
all_mute = args.mute
while i<len(arrays)-1:
  filters = arrays[i].split(",")
  startTime = filters[0].replace(":", "\\\\:")
  endTime = arrays[i+1].split(",")[0].replace(":", "\\\\:")
  trim = "trim=start=%s:end=%s"%(startTime, endTime)
  video += "[0:v]"+trim+",setpts=PTS-STARTPTS"
  if not all_mute:
    audio += "[0:a]a"+trim+",asetpts=PTS-STARTPTS"
  if len(filters)>1:
    for filter in filters[1:]:
      filter = filter.split("=")
      if filter[0]=="speed" or filter[0]=="speedup" or filter[0]=="speedown":
        video += ",setpts=PTS/"+filter[1]
        if not all_mute:
          if len(filter)>2:
            if filter[2]==mute:
              pass
            else:
              audio += ",atempo="+filter[1]
          else:
            audio += ",atempo="+filter[1]
      if filter[0]=="crop":
        video += ",crop="+filter[1]
  video += ("[v%s]"%str(iv))+";"
  iv += 1
  if not all_mute:
    audio += ("[a%s]"%str(ia))+";"
    ia += 1
  i = i+1

map = ""
filter_complex = video+audio
for i in range(0, iv): filter_complex+="[v{}]".format(i)
filter_complex+="concat=n=%s:v=1:a=0[out_v]"%iv
map += "-map [out_v]"
if ia>0:
  filter_complex+=";"
  for i in range(0, ia): filter_complex+="[a{}]".format(i)
  filter_complex+="concat=n=%s:v=0:a=1[out_a]"%ia
  map += " -map [out_a]"
command = "ffmpeg -i \"{}\" -filter_complex \"{}\" {} -c:v h264 -c:a aac \"{}\"".format(input, filter_complex, map, output)
print(command)
