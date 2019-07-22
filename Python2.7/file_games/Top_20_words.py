
import operator

## Print the Top 20 Words

def rank_words(f):
	"""
		Takes in a file, then ranks all the words within the file
		
		Args: a file
		
		Return: A sorted list of tuples
	"""
	word_dict = {} # Start with empty python Dictionary
	words = [] # Start with empty python List
	for line in f:
		list_of_words = line.split()
		for w in list_of_words:
			words.append(w.lower()) # Add Word to List

	for word in words:
		if word_dict.has_key(word):
			word_dict[word] += 1 # Incr. value in Dict.
		else:
			word_dict[word] = 1 # Add word and value to Dict.
        # This will sort the dictionary and return a list of Tuples
	return sorted(word_dict.iteritems(), reverse=True, \
					key=operator.itemgetter(1))


def main():
	# Files
	name = str(raw_input("Enter the file name located in this directory: "))
	f = open(name, 'rU')

	ranked_words_list = rank_words(f)

	f.close()

        # Print the results
	for w in list(ranked_words_list[:20]):
		print w[0],"---", w[1]


if __name__ == '__main__':
	main()

