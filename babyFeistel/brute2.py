from subprocess import check_output

alphabetLowerCase = [chr(i) for i in range(97, 123)]
# alphabetUpperCase = [chr(i) for i in range(65, 91)]
alphabet = alphabetLowerCase
# alphabet = [chr(i) for i in range(48, 91)]
# alphabet += [chr(i) for i in range(97, 126)]

# keys=[]
# keys = ['{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{', '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}', 'owevunremofrmleaaiowevunremofrmleaai', 'pxfwvosfnpgsnmfbbjqygxwptgoqhtongcck', 'qygxwptgoqhtongccksaizyrviqsjvqpieem', 'rzhyxquhpriupohddluckbatxksulxsrkggo', 'saizyrviqsjvqpieemwemdcvzmuwnzutmiiq', 'tbjazswjrtkwrqjffnygofexbowypbwvokks', 'uckbatxksulxsrkggoaiqhgzdqyardyxqmmu', 'vdlcbuyltvmytslhhpcksjibfsactfazsoow', 'wemdcvzmuwnzutmiiqemulkdhucevhcbuqqy', 'xfnedwanvxoavunjjrgownmfjwegxjedwssa', 'ygofexbowypbwvokksiqypohlygizlgfyuuc', 'zhpgfycpxzqcxwplltksarqjnaikbnihawwe', 'aiqhgzdqyardyxqmmumuctslpckmdpkjcyyg', 'bjrihaerzbsezyrnnvowevunremofrmleaai', 'cksjibfsactfazsoowqygxwptgoqhtongcck', 'dltkjcgtbdugbatppxsaizyrviqsjvqpieem', 'emulkdhucevhcbuqqyuckbatxksulxsrkggo', 'fnvmleivdfwidcvrrzwemdcvzmuwnzutmiiq', 'gownmfjwegxjedwssaygofexbowypbwvokks', 'hpxongkxfhykfexttbaiqhgzdqyardyxqmmu', 'iqypohlygizlgfyuuccksjibfsactfazsoow', 'jrzqpimzhjamhgzvvdemulkdhucevhcbuqqy', 'ksarqjnaikbnihawwegownmfjwegxjedwssa', 'ltbsrkobjlcojibxxfiqypohlygizlgfyuuc', 'muctslpckmdpkjcyygksarqjnaikbnihawwe', 'nvdutmqdlneqlkdzzhmuctslpckmdpkjcyyg', 'OWEVUNREMOFRMLEAAIOWEVUNREMOFRMLEAAI', 'PXFWVOSFNPGSNMFBBJQYGXWPTGOQHTONGCCK', 'QYGXWPTGOQHTONGCCKSAIZYRVIQSJVQPIEEM', 'RZHYXQUHPRIUPOHDDLUCKBATXKSULXSRKGGO', 'SAIZYRVIQSJVQPIEEMWEMDCVZMUWNZUTMIIQ', 'TBJAZSWJRTKWRQJFFNYGOFEXBOWYPBWVOKKS', 'UCKBATXKSULXSRKGGOAIQHGZDQYARDYXQMMU', 'VDLCBUYLTVMYTSLHHPCKSJIBFSACTFAZSOOW', 'WEMDCVZMUWNZUTMIIQEMULKDHUCEVHCBUQQY', 'XFNEDWANVXOAVUNJJRGOWNMFJWEGXJEDWSSA', 'YGOFEXBOWYPBWVOKKSIQYPOHLYGIZLGFYUUC', 'ZHPGFYCPXZQCXWPLLTKSARQJNAIKBNIHAWWE', 'AIQHGZDQYARDYXQMMUMUCTSLPCKMDPKJCYYG', 'BJRIHAERZBSEZYRNNVOWEVUNREMOFRMLEAAI', 'CKSJIBFSACTFAZSOOWQYGXWPTGOQHTONGCCK', 'DLTKJCGTBDUGBATPPXSAIZYRVIQSJVQPIEEM', 'EMULKDHUCEVHCBUQQYUCKBATXKSULXSRKGGO', 'FNVMLEIVDFWIDCVRRZWEMDCVZMUWNZUTMIIQ', 'GOWNMFJWEGXJEDWSSAYGOFEXBOWYPBWVOKKS', 'HPXONGKXFHYKFEXTTBAIQHGZDQYARDYXQMMU', 'IQYPOHLYGIZLGFYUUCCKSJIBFSACTFAZSOOW', 'JRZQPIMZHJAMHGZVVDEMULKDHUCEVHCBUQQY', 'KSARQJNAIKBNIHAWWEGOWNMFJWEGXJEDWSSA', 'LTBSRKOBJLCOJIBXXFIQYPOHLYGIZLGFYUUC', 'MUCTSLPCKMDPKJCYYGKSARQJNAIKBNIHAWWE', 'NVDUTMQDLNEQLKDZZHMUCTSLPCKMDPKJCYYG']
# output = "dhiNweztfCFemWmsE}hpbFwitltWXsgImkM}"
# result = []
bracket = '}'

for i in alphabet:
  print(i)
  command = f"echo 'pleScriptOAnaLisE{bracket}{i*3}Fb{i}b{i*2}EJ{i}k{i}efG{bracket}' | nc 3.135.153.98 4000"
  try:
    output = check_output(command, shell=True).decode("utf-8")
    # keys.append(output.split(": ")[2][:-1])
    print(output.split(": ")[2])
  except:
    print("error")
    exit(1)

# print(keys)

# for i in range(len(output)):
#   for j in range(len(keys)):
#     if list(keys[j])[i] == output[i]:
#       result.append(alphabet[j])
#       break
#     if (j == len(keys) - 1):
#       print(f'{i} {output[i]}')
#       # result.append(output[i])
#       result.append('?')
#       # exit(1)

# print(''.join(result))