#
# SMSParser.py - Code snippet to parse an incoming SMS message (text format) using regular expressions
#



import re



    for Msg in SMSList:
      # parse a single sms message using regular expressions
      Match = []
      Match = re.findall( "\+CMGL: (\d+),""(.+)"",""(.+)"",(.*),""(.+)""\r\n(.+)\r\n", Msg ) # returns a list of lists

      for Each in Match:
        # needed data in Each[ 0 ] ... Each[ n ]

# EOF
