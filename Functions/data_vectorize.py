from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

def vectorize(Text) :
    return TfidfVectorizer(analyzer="char").fit_transform(Text).toarray()

# similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

def similarity(doc1,doc2) :
    return cosine_similarity([doc1,doc2])

def check_plagiarism(TestFiles, sample_files):
    vectors = vectorize(TestFiles)
    s_vectors = list(zip(sample_files, vectors))
    results = set()
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], sim_score
            results.add(score)
    return results

def ExecutePlagiarismChecker(ArrayToTest, sample_files):
    for array_index in range(len(ArrayToTest)):
        temp_text = ""
        for item_index in range(len(ArrayToTest[array_index])):
            temp_text += ArrayToTest[array_index][item_index]
        ArrayToTest[array_index] = temp_text
    return check_plagiarism(ArrayToTest, sample_files)