# -*- coding:utf-8 -*-
import csv

RATE_BONUS = 0.02/2
RATE_MONTH = 0.02/12
MANSION_COST = int (input ('マンションの金額○ 万円>>  ') ) * 10000
BONUS = int (input ('ボーナスの月に払う金額○ 万円>>  ') ) * 10000
YEAR = int (input('返済期間○ 年>>  '))
MONTH = 12 * YEAR

def calc_payment_bonus(return_payment):
	payment_month = (return_payment * RATE_MONTH * (1 + RATE_MONTH)**MONTH) / ((1 + RATE_MONTH)**MONTH - 1)
	return payment_month

def get_bonus_payment(bonus):
        bonus_pay = bonus * RATE_BONUS *(1 + RATE_BONUS) ** 2 / ((1 + RATE_BONUS) ** 2 - 1) 
        return bonus_pay

def get_interest(payment):
	interest = payment * RATE_MONTH 
	return interest

if __name__ == '__main__':
	paid = 0
	bonus_all = 0
	bonus_payment = MONTH / 6 * BONUS

	#配列の初期化
	A_payment_month = (MONTH + 1) * [0]
	A_payment_left = (MONTH + 1) * [0]
	A_paid= (MONTH + 1) * [0]
	A_interest = (MONTH + 1) * [0]
	A_bonus = (MONTH + 1) * [0]
	cs = []

	#配列の一文字目
	A_payment_month[0] = '月の支払い'
	A_payment_left[0] = '残りの支払い'
	A_paid[0] = '支払い済み'
	A_interest[0] = '利子'
	A_bonus[0] = 'ボーナス'

	#初期値代入
	payment_left = MANSION_COST
	#ボーナス合計をひいた残りの総支払額
	payment_left_bonus = MANSION_COST - bonus_payment

	#シミュレーションを行う
	for i in range(1, MONTH + 1):
		#ボーナス支払い月
		if i % 6 == 1 :
			A_bonus[i] = BONUS	
			print('now',payment_left)
			payment_left = payment_left - BONUS
			print('bonus',payment_left)

			bonus_all += BONUS
			paid += BONUS
		
		#利子の計算
		interest = get_interest(payment_left)
		A_interest[i] = interest

		#月々の支払額
		if i == MONTH :
			payment_month = payment_left + interest
			print('last month')
		else:
			payment_month = calc_payment_bonus(payment_left_bonus)
		
		A_payment_month[i] = payment_month
		
		#残りの支払い額
		payment_left = payment_left + interest -payment_month
		A_payment_left[i] = payment_left
		
		#payment_left_bonus = payment_left_bonus + interest -payment_month

		#支払済み
		paid += payment_month
		A_paid[i] = paid

	#CSVの書き込みを行う
	f = open('bonus%d_pay%d.csv' % (BONUS,MANSION_COST), 'w')
	writer_csv = csv.writer(f)

	for j in range(MONTH + 1):
		if j == 0:
			cs.append('月')
		else:
			cs.append(j)

		cs.append(A_payment_month[j])
		cs.append(A_payment_left[j])
		cs.append(A_paid[j])
		cs.append(A_interest[j])
		cs.append( A_bonus[j])

		writer_csv.writerow(cs)

		cs = []

	f.close()
	print(bonus_all)
