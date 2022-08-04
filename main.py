from logic import *
P,Q,R = vars('P', 'Q', 'R')
formula0 = ~P
formula1 = P&Q
formula2 = P|Q
formula3 = P>>Q
formula4 = P.iff(Q)

formula0.print_truth_table()
formula1.print_truth_table()
formula2.print_truth_table()
formula3.print_truth_table()
formula4.print_truth_table()