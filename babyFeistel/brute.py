from subprocess import check_output

alphabetLowerCase = [chr(i) for i in range(97, 123)]
alphabetUpperCase = [chr(i) for i in range(65, 91)]
alphabet = alphabetLowerCase + alphabetUpperCase
# alphabet = [chr(i) for i in range(48, 91)]
# alphabet += [chr(i) for i in range(97, 126)]

keys=[]
# keys = ['owevunremofrmleaa}sexnunremofrmleaa}', 'pxfwvosfnpgsnmfbb}tfyovptgoqhtongcc}', 'qygxwptgoqhtongcc}ugzpwrviqsjvqpiee}', 'rzhyxquhpriupohdd}vhaqxtxksulxsrkgg}', 'saizyrviqsjvqpiee}wibryvzmuwnzutmii}', 'tbjazswjrtkwrqjff}xjcszxbowypbwvokk}', 'uckbatxksulxsrkgg}ykdtazdqyardyxqmm}', 'vdlcbuyltvmytslhh}zleubbfsactfazsoo}', 'wemdcvzmuwnzutmii}amfvcdhucevhcbuqq}', 'xfnedwanvxoavunjj}bngwdfjwegxjedwss}', 'ygofexbowypbwvokk}cohxehlygizlgfyuu}', 'zhpgfycpxzqcxwpll}dpiyfjnaikbnihaww}', 'aiqhgzdqyardyxqmm}eqjzglpckmdpkjcyy}', 'bjrihaerzbsezyrnn}frkahnremofrmleaa}', 'cksjibfsactfazsoo}gslbiptgoqhtongcc}', 'dltkjcgtbdugbatpp}htmcjrviqsjvqpiee}', 'emulkdhucevhcbuqq}iundktxksulxsrkgg}', 'fnvmleivdfwidcvrr}jvoelvzmuwnzutmii}', 'gownmfjwegxjedwss}kwpfmxbowypbwvokk}', 'hpxongkxfhykfextt}lxqgnzdqyardyxqmm}', 'iqypohlygizlgfyuu}myrhobfsactfazsoo}', 'jrzqpimzhjamhgzvv}nzsipdhucevhcbuqq}', 'ksarqjnaikbnihaww}oatjqfjwegxjedwss}', 'ltbsrkobjlcojibxx}pbukrhlygizlgfyuu}', 'muctslpckmdpkjcyy}qcvlsjnaikbnihaww}', 'nvdutmqdlneqlkdzz}rdwmtlpckmdpkjcyy}', 'OWEVUNREMOFRMLEAA}SEXNUNREMOFRMLEAA}', 'PXFWVOSFNPGSNMFBB}TFYOVPTGOQHTONGCC}', 'QYGXWPTGOQHTONGCC}UGZPWRVIQSJVQPIEE}', 'RZHYXQUHPRIUPOHDD}VHAQXTXKSULXSRKGG}', 'SAIZYRVIQSJVQPIEE}WIBRYVZMUWNZUTMII}', 'TBJAZSWJRTKWRQJFF}XJCSZXBOWYPBWVOKK}', 'UCKBATXKSULXSRKGG}YKDTAZDQYARDYXQMM}', 'VDLCBUYLTVMYTSLHH}ZLEUBBFSACTFAZSOO}', 'WEMDCVZMUWNZUTMII}AMFVCDHUCEVHCBUQQ}', 'XFNEDWANVXOAVUNJJ}BNGWDFJWEGXJEDWSS}', 'YGOFEXBOWYPBWVOKK}COHXEHLYGIZLGFYUU}', 'ZHPGFYCPXZQCXWPLL}DPIYFJNAIKBNIHAWW}', 'AIQHGZDQYARDYXQMM}EQJZGLPCKMDPKJCYY}', 'BJRIHAERZBSEZYRNN}FRKAHNREMOFRMLEAA}', 'CKSJIBFSACTFAZSOO}GSLBIPTGOQHTONGCC}', 'DLTKJCGTBDUGBATPP}HTMCJRVIQSJVQPIEE}', 'EMULKDHUCEVHCBUQQ}IUNDKTXKSULXSRKGG}', 'FNVMLEIVDFWIDCVRR}JVOELVZMUWNZUTMII}', 'GOWNMFJWEGXJEDWSS}KWPFMXBOWYPBWVOKK}', 'HPXONGKXFHYKFEXTT}LXQGNZDQYARDYXQMM}', 'IQYPOHLYGIZLGFYUU}MYRHOBFSACTFAZSOO}', 'JRZQPIMZHJAMHGZVV}NZSIPDHUCEVHCBUQQ}', 'KSARQJNAIKBNIHAWW}OATJQFJWEGXJEDWSS}', 'LTBSRKOBJLCOJIBXX}PBUKRHLYGIZLGFYUU}', 'MUCTSLPCKMDPKJCYY}QCVLSJNAIKBNIHAWW}', 'NVDUTMQDLNEQLKDZZ}RDWMTLPCKMDPKJCYY}']
# keys = ['{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{', '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}', 'owevunremofrmleaaiowevunremofrmleaai', 'pxfwvosfnpgsnmfbbjqygxwptgoqhtongcck', 'qygxwptgoqhtongccksaizyrviqsjvqpieem', 'rzhyxquhpriupohddluckbatxksulxsrkggo', 'saizyrviqsjvqpieemwemdcvzmuwnzutmiiq', 'tbjazswjrtkwrqjffnygofexbowypbwvokks', 'uckbatxksulxsrkggoaiqhgzdqyardyxqmmu', 'vdlcbuyltvmytslhhpcksjibfsactfazsoow', 'wemdcvzmuwnzutmiiqemulkdhucevhcbuqqy', 'xfnedwanvxoavunjjrgownmfjwegxjedwssa', 'ygofexbowypbwvokksiqypohlygizlgfyuuc', 'zhpgfycpxzqcxwplltksarqjnaikbnihawwe', 'aiqhgzdqyardyxqmmumuctslpckmdpkjcyyg', 'bjrihaerzbsezyrnnvowevunremofrmleaai', 'cksjibfsactfazsoowqygxwptgoqhtongcck', 'dltkjcgtbdugbatppxsaizyrviqsjvqpieem', 'emulkdhucevhcbuqqyuckbatxksulxsrkggo', 'fnvmleivdfwidcvrrzwemdcvzmuwnzutmiiq', 'gownmfjwegxjedwssaygofexbowypbwvokks', 'hpxongkxfhykfexttbaiqhgzdqyardyxqmmu', 'iqypohlygizlgfyuuccksjibfsactfazsoow', 'jrzqpimzhjamhgzvvdemulkdhucevhcbuqqy', 'ksarqjnaikbnihawwegownmfjwegxjedwssa', 'ltbsrkobjlcojibxxfiqypohlygizlgfyuuc', 'muctslpckmdpkjcyygksarqjnaikbnihawwe', 'nvdutmqdlneqlkdzzhmuctslpckmdpkjcyyg', 'OWEVUNREMOFRMLEAAIOWEVUNREMOFRMLEAAI', 'PXFWVOSFNPGSNMFBBJQYGXWPTGOQHTONGCCK', 'QYGXWPTGOQHTONGCCKSAIZYRVIQSJVQPIEEM', 'RZHYXQUHPRIUPOHDDLUCKBATXKSULXSRKGGO', 'SAIZYRVIQSJVQPIEEMWEMDCVZMUWNZUTMIIQ', 'TBJAZSWJRTKWRQJFFNYGOFEXBOWYPBWVOKKS', 'UCKBATXKSULXSRKGGOAIQHGZDQYARDYXQMMU', 'VDLCBUYLTVMYTSLHHPCKSJIBFSACTFAZSOOW', 'WEMDCVZMUWNZUTMIIQEMULKDHUCEVHCBUQQY', 'XFNEDWANVXOAVUNJJRGOWNMFJWEGXJEDWSSA', 'YGOFEXBOWYPBWVOKKSIQYPOHLYGIZLGFYUUC', 'ZHPGFYCPXZQCXWPLLTKSARQJNAIKBNIHAWWE', 'AIQHGZDQYARDYXQMMUMUCTSLPCKMDPKJCYYG', 'BJRIHAERZBSEZYRNNVOWEVUNREMOFRMLEAAI', 'CKSJIBFSACTFAZSOOWQYGXWPTGOQHTONGCCK', 'DLTKJCGTBDUGBATPPXSAIZYRVIQSJVQPIEEM', 'EMULKDHUCEVHCBUQQYUCKBATXKSULXSRKGGO', 'FNVMLEIVDFWIDCVRRZWEMDCVZMUWNZUTMIIQ', 'GOWNMFJWEGXJEDWSSAYGOFEXBOWYPBWVOKKS', 'HPXONGKXFHYKFEXTTBAIQHGZDQYARDYXQMMU', 'IQYPOHLYGIZLGFYUUCCKSJIBFSACTFAZSOOW', 'JRZQPIMZHJAMHGZVVDEMULKDHUCEVHCBUQQY', 'KSARQJNAIKBNIHAWWEGOWNMFJWEGXJEDWSSA', 'LTBSRKOBJLCOJIBXXFIQYPOHLYGIZLGFYUUC', 'MUCTSLPCKMDPKJCYYGKSARQJNAIKBNIHAWWE', 'NVDUTMQDLNEQLKDZZHMUCTSLPCKMDPKJCYYG']
# keys = ['dhiNweztfCFemWmsE}hpbFweztfCFemWmsE}', 'dhiNweztfCFemWmsE}hpbFwfaugDGfnXntF}', 'dhiNweztfCFemWmsE}hpbFwgbvhEHgoYouG}', 'dhiNweztfCFemWmsE}hpbFwhcwiFIhpZpvH}', 'dhiNweztfCFemWmsE}hpbFwidxjGJiqAqwI}', 'dhiNweztfCFemWmsE}hpbFwjeykHKjrBrxJ}', 'dhiNweztfCFemWmsE}hpbFwkfzlILksCsyK}', 'dhiNweztfCFemWmsE}hpbFwlgamJMltDtzL}', 'dhiNweztfCFemWmsE}hpbFwmhbnKNmuEuaM}', 'dhiNweztfCFemWmsE}hpbFwnicoLOnvFvbN}', 'dhiNweztfCFemWmsE}hpbFwojdpMPowGwcO}', 'dhiNweztfCFemWmsE}hpbFwpkeqNQpxHxdP}', 'dhiNweztfCFemWmsE}hpbFwqlfrORqyIyeQ}', 'dhiNweztfCFemWmsE}hpbFwrmgsPSrzJzfR}', 'dhiNweztfCFemWmsE}hpbFwsnhtQTsaKagS}', 'dhiNweztfCFemWmsE}hpbFwtoiuRUtbLbhT}', 'dhiNweztfCFemWmsE}hpbFwupjvSVucMciU}', 'dhiNweztfCFemWmsE}hpbFwvqkwTWvdNdjV}', 'dhiNweztfCFemWmsE}hpbFwwrlxUXweOekW}', 'dhiNweztfCFemWmsE}hpbFwxsmyVYxfPflX}', 'dhiNweztfCFemWmsE}hpbFwytnzWZygQgmY}', 'dhiNweztfCFemWmsE}hpbFwzuoaXAzhRhnZ}', 'dhiNweztfCFemWmsE}hpbFwavpbYBaiSioA}', 'dhiNweztfCFemWmsE}hpbFwbwqcZCbjTjpB}', 'dhiNweztfCFemWmsE}hpbFwcxrdADckUkqC}', 'dhiNweztfCFemWmsE}hpbFwdyseBEdlVlrD}', 'dhiNweztfCFemWmsE}hpbFweztfCFemWmsE}', 'dhiNweztfCFemWmsE}hpbFwfaugDGfnXntF}', 'dhiNweztfCFemWmsE}hpbFwgbvhEHgoYouG}', 'dhiNweztfCFemWmsE}hpbFwhcwiFIhpZpvH}', 'dhiNweztfCFemWmsE}hpbFwidxjGJiqAqwI}', 'dhiNweztfCFemWmsE}hpbFwjeykHKjrBrxJ}', 'dhiNweztfCFemWmsE}hpbFwkfzlILksCsyK}', 'dhiNweztfCFemWmsE}hpbFwlgamJMltDtzL}', 'dhiNweztfCFemWmsE}hpbFwmhbnKNmuEuaM}', 'dhiNweztfCFemWmsE}hpbFwnicoLOnvFvbN}', 'dhiNweztfCFemWmsE}hpbFwojdpMPowGwcO}', 'dhiNweztfCFemWmsE}hpbFwpkeqNQpxHxdP}', 'dhiNweztfCFemWmsE}hpbFwqlfrORqyIyeQ}', 'dhiNweztfCFemWmsE}hpbFwrmgsPSrzJzfR}', 'dhiNweztfCFemWmsE}hpbFwsnhtQTsaKagS}', 'dhiNweztfCFemWmsE}hpbFwtoiuRUtbLbhT}', 'dhiNweztfCFemWmsE}hpbFwupjvSVucMciU}', 'dhiNweztfCFemWmsE}hpbFwvqkwTWvdNdjV}', 'dhiNweztfCFemWmsE}hpbFwwrlxUXweOekW}', 'dhiNweztfCFemWmsE}hpbFwxsmyVYxfPflX}', 'dhiNweztfCFemWmsE}hpbFwytnzWZygQgmY}', 'dhiNweztfCFemWmsE}hpbFwzuoaXAzhRhnZ}', 'dhiNweztfCFemWmsE}hpbFwavpbYBaiSioA}', 'dhiNweztfCFemWmsE}hpbFwbwqcZCbjTjpB}', 'dhiNweztfCFemWmsE}hpbFwcxrdADckUkqC}', 'dhiNweztfCFemWmsE}hpbFwdyseBEdlVlrD}']
output = "dhiNweztfCFemWmsE}hpbFwitltWXsgImkM}"
result = []

for i in alphabet:
  print(i)
  command = f'echo "eits{{eusousouma{i*3}pleScriptOAnaLisE}}" | nc 3.135.153.98 4000'
  try:
    commandOutput = check_output(command, shell=True).decode("utf-8")
    keys.append(commandOutput.split(": ")[2][:-1])
    print(commandOutput.split(": ")[2])
  except:
    print("error")
    exit(1)

print(keys)

count = 0

for i in range(len(output)):
  result.append('|')
  for j in range(len(keys)):
    if list(keys[j])[i] == output[i]:
      result.append(alphabet[j])
      count = 1
    if (j == len(keys) - 1 and count == 0):
      print(f'{i} {output[i]}')
      # result.append(output[i])
      result.append('?')
      # exit(1)
  count = 0

print(''.join(result))