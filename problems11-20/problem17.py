"""
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
	dir
	    subdir1
	    subdir2
	        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
	dir
	    subdir1
	        file1.ext
	        subsubdir1
	    subdir2
	        subsubdir2
	            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext. We are interested in finding the longest (number of characters) absolute path to a file within our file
system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes). Given a string representing the file system in the above 
format, return the length of the longest absolute path to a file in the abstracted file system. If there is no ]
file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.

PS.
String output it's for visual contents
"""
from collections import Counter


# from the end to the beginning
def longest_path(path):
	path = path.split('\n')
	le = len(path) - 1
	maxi = 0
	longest = '' # for visual
	
	for f in path:
		if '.' not in f:
			continue

		ts = Counter(f)['\t']
		total = len(f[ts:]) + 1
		dirs = [f[ts:]] # for visual
		idx = path.index(f)
		while idx >= 0:
			count = Counter(path[idx])['\t']
			if count == ts-1:
				total += len(path[idx][count:])
				if count != 0: total += 1
				dirs.append(path[idx][count:]) # for visual
				ts -= 1
			idx -= 1
		maxi = max(total, maxi)
		# for visual
		if len('/'.join(dirs)) > len(longest):
			longest = '/'.join(dirs[::-1])

	print(longest) # for visual
	return maxi


# from end to beginning
def longest_path_two(path):
	longest = 0

	for tkid, tk in enumerate(path.split('\n')[::-1]):
		if '.' not in tk:
			continue

		dirs = [tk.strip('\t\t')]
		tabs = len(tk) - len(tk.strip('\t\t'))
		# for dr in path.split('\n')[::-1]:
		for dr in path.split('\n')[::-1][tkid:]:
			if '.' in dr:
				continue

			print(dr)

			if (len(dr) - len(dr.strip('\t\t')) == tabs - 1):
				dirs.append(dr.strip('\t\t'))
				tabs -= 1

		longest = max(longest, len('/'.join(dirs)))

	return longest


# from the beginning to the end
# This Solutions from (https://github.com/r1cc4rdo/daily_coding_problem)
# which was a great tool for learning
def longest_path_three(path):
	longest = 0
	folders = [None]

	for token in path.split('\n'):
		tabs = 0
		while token[tabs] == '\t':
			tabs += 1
			
		# shouldn't happen
		if tabs > len(folders):
			# too deep for example. dir\n\t\tsubdir1 it's impossible
			break

		if tabs == len(folders):
			# file shouldn't have other files or dirs
			if '.' in folders[-1]:
				break
			folders.append(None)
		else:
			folders = folders[:tabs + 1]

		folders[-1] = str.strip(token)
		if '.' in folders[-1]:
			longest = max(longest, len('/'.join(folders)))

	return longest
		

def main():
	path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
	path2 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
	print(longest_path(path))
	print(longest_path_three(path))
	print(longest_path_two(path))


if __name__ == '__main__':
	main()
