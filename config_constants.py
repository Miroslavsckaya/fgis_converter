import yaml

try:
    config_file = open('./config/company_config.local.yml')
except:
    config_file = open('./config/company_config.yml')

company_config = yaml.safe_load(config_file)

with open('./config/registration_numbers.yml') as f:
    valid_reg_nums = yaml.safe_load(f)

config_file.close()