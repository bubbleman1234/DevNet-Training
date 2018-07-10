
def main():
	Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
	count_session = 1

	for i in Sessions_Attended['sessions']:
		if i == ',':
			count_session += 1

	print("I have attended  %d sessions!!" %count_session)

if __name__ == '__main__':
	main()
