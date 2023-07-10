from os import listdir
from json import load as js_load

ALGOS = (
	('sha1', 0),
	('sha256', 1),
	('sha512', 2),
	('steam', 3)
)

FN = 'totp.conf'

jsons = list(
	filter(
		lambda fn : fn.endswith('.json'), listdir('.')
	)
)

def check_algo(alg: str) -> int:
	n_alg = alg.lower()
	t_alg = -1

	for alg, idd in ALGOS:
		if alg in n_alg:
			t_alg = idd
			break

	return t_alg

with open(FN, 'a') as f_totp:
	for fn in jsons:
		with open(fn) as f:
			totp_datas = js_load(f)

			for totp_data in totp_datas:
				alg = check_algo(totp_data['algorithm'])
				
				if alg == -1:
					print(f"{totp_data['name']} has Alg '{totp_data['algorithm']}' that isn't supported")
					continue
				
				totp_secret = totp_data['totpSecret'].replace('=', '')
				line = f"\nTokenName: {totp_data['name']}\n"
				line += f"TokenSecret: {totp_secret}\n"
				line += f"TokenAlgo: {alg}\n"
				f_totp.write(line)
			