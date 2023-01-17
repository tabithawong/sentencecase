# code for converting json values to sentence case

# NOTES:
# - leaves values that are completely uppercase untouched
# - converts to sentence case as long as the value is in title case or has a capitalized word in its middle
# - add to acronym list to ensure that acronyms stay in uppercase

# acronym list
acronyms = ["TFSA", "RRSP", "ID", "LIRA", "RRIF", "LIF", "PEP", "HIO"]

# reading the lines from the input file to an array
with open('literals.txt', 'r') as reader:
  lines = reader.readlines()

# writing to an output file
with open('scliterals.txt', 'w') as writer:
  
  # iterating through the array of lines
  for line in lines:
    
    # if the line has "value:" in it
    if ('"value":' in line):
      # splitting the line by the quotation marks in it
      linearr = line.split("\"")
      # extracting the value after : in the line
      value = linearr[3]

      # if the value is not structured in the "or" format
      if (len(linearr) < 6):
        # if the value is not already in sentence case and not all uppercase and it does not contain a placeholder
        if ((value != value.capitalize()) and (value != value.upper())):
          
          # if no placeholder and no sentence in value
          if ((value.__contains__("$") == False) and (value.__contains__(". ") == False)):
            # converting the value to sentence case using the built-in capitalize function, which makes only the first character a capital
            sc = value.capitalize()

            # replacing all acronyms with uppercases
            for i in range(0, len(acronyms)):
              if (sc.upper().__contains__(acronyms[i])):
                uppervalue = sc.replace(acronyms[i].lower(), acronyms[i])
                sc = uppervalue
            
            # reconstructing the line with the same formatting as before
            scline = '        "' + linearr[1] + '"' + linearr[2] + '"' + sc + '",'
            # writing the newly reconstructed line to the output file
            writer.write(scline + '\n')
            
          # if placeholder in value  
          elif (value.__contains__("$")):
            # split value by $
            valuearr = value.split("$")

            for i in range(0, len(valuearr)):

              # looking at part of the value before the variable placeholder
              if (i == 0):

                # if no "(" in the part before 
                if (valuearr[i].__contains__("(") == False):
                  temp = valuearr[i].capitalize()
                  valuearr[i] = temp

                # if "(" is in the part before
                else:
                  brackarr = valuearr[i].split("(")
                  temp1 = brackarr[0].capitalize()
                  brackarr[0] = temp1
                  temp = "(".join(brackarr)
                  valuearr[i] = temp

              # making the text after ($variableName) lowercase
              elif (i > 1):
                temp = valuearr[i].lower()
                valuearr[i] = temp

            sc = "$".join(valuearr)

            # replacing all acronyms with uppercases
            for i in range(0, len(acronyms)):
              if (sc.upper().__contains__(acronyms[i])):
                uppervalue = sc.replace(acronyms[i].lower(), acronyms[i])
                sc = uppervalue
            scline = '        "' + linearr[1] + '"' + linearr[2] + '"' + sc + '",'
            writer.write(scline + '\n')
            
          # if sentence in value
          elif (value.__contains__(". ")):
            # split value by periods that end sentences
            valuearr = value.split(". ")

            for i in range (0, len(valuearr)):
              temp = valuearr[i].capitalize()
              valuearr[i] = temp

            sc = ". ".join(valuearr)

            # replacing all acronyms with uppercases
            for i in range(0, len(acronyms)):
              if (sc.upper().__contains__(acronyms[i])):
                uppervalue = sc.replace(acronyms[i].lower(), acronyms[i])
                sc = uppervalue
            scline = '        "' + linearr[1] + '"' + linearr[2] + '"' + sc + '",'
            writer.write(scline + '\n')
            
        else:
          # write the line from input to output as is
          writer.write(line)
          
      else:
        # write the line from input to output as is
        writer.write(line)
        
    else:
      # write the line from input to output as is
      writer.write(line)

