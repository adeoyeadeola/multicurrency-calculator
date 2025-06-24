# Write code below 💖
a = int(input('what do you have left in pesos?'))
b = int(input('what do you have left in soles?'))
c = int(input('what do you have left in reais?'))
conversion_rates_to_usd = { 'pesos': 4085  , 'soles': 3.59 ,'reais':5.50 }
#convert to usd
usd_from_pesos = a/ conversion_rates_to_usd['pesos']
usd_from_soles = b/ conversion_rates_to_usd['soles']
usd_from_reais = c/ conversion_rates_to_usd['reais']
# total in usd
total_in_usd = usd_from_pesos + usd_from_soles + usd_from_reais
print('total_in_usd is ', round(total_in_usd, 2))
