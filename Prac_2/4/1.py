def generate_groups(program_code='ИКБО', start_year=22, num_groups=27):
    return [f'{program_code}-{str(i).zfill(2)}-{start_year}' for i in range(1, num_groups+1)]


result = generate_groups()
print(result)
