def luh(card_number):
  clean_card_number = "".join(digit for digit in card_number if digit.isdigit())
  print(clean_card_number)
  reversed_card_number = ""
  

  odd_numbers = clean_card_number[-2::-2]
  even_numbers = clean_card_number[-1::-2]
  print(odd_numbers, even_numbers)

  total_even_numbers = sum(map(int, even_numbers))
  total_odd_numbers = 0

  for number in odd_numbers:
    duplicated = int(number) * 2
    if duplicated >= 10:
      total_odd_numbers += (duplicated // 10 + duplicated % 10)
    else:
      total_odd_numbers += duplicated  
  print(total_even_numbers, total_odd_numbers)

  total_sum = total_odd_numbers + total_even_numbers
  
  if total_sum % 10 == 0:
    return True
  return False  

print(luh("499-2739-8716"))