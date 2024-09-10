slices = int(input('how many slices?'))
pizza = slices // 4
print(f'pizza = {slices // 4}')
# if slices % 4 != 0:
# if not slices % 4 == 0:
if slices % 4 != 0:
    print(f'another pizza for {slices % 4}')


