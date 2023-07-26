import os


def index_of_part() -> int:
    """Return index of where the Part_2 begins"""
    index = 0
    for i, el in enumerate(book_list):
        if "PART II." in el:
            index = i
    return index


def make_part12_folders() -> None:
    """Makes Part_1 and Part_2 folders, and inside them makes CHAPTER_num_of_chapter folders"""
    os.mkdir("Part_1")
    os.mkdir("Part_2")

    counter_1 = 0
    for i in range(index_of_part()):
        if "CHAPTER" in book_list[i]:
            counter_1 += 1
            os.mkdir(f"Part_1/CHAPTER_{counter_1}")

    counter_2 = 0
    for j in range(index_of_part(), len(book_list)):
        if "CHAPTER" in book_list[j]:
            counter_2 += 1
            os.mkdir(f"Part_2/CHAPTER_{counter_2}")


def num_of_chapters() -> tuple:
    """Returns numbers of chapters in each part"""
    chapters_part_1 = len(next(os.walk('Part_1'))[1])
    chapters_part_2 = len(next(os.walk('Part_2'))[1])
    return chapters_part_1, chapters_part_2


def name_of_file_list():
    """Returns a list of names of each of the chapters"""
    list_of_names = []
    list_of_names_unchanged = []
    for i in range(len(book_list)):
        if "CHAPTER" in book_list[i]:
            list_of_names.append(book_list[i+2].replace("\n", "").strip())
            list_of_names_unchanged.append(book_list[i+2])
    return list_of_names, list_of_names_unchanged


def text_from_chapter():
    """Returns a list. Elements of that list are texts from each chapter respectively"""
    text_from_chapter_list = []
    indexes_of_names = []
    for name in name_of_file_list()[1]:
        index_of_name = book_list.index(name)
        indexes_of_names.append(index_of_name)

    for i in range(len(indexes_of_names) - 1):
        text_list = book_list[indexes_of_names[i] + 2:indexes_of_names[i + 1] - 6]
        text = ""
        for el in text_list:
            text += el
        text_from_chapter_list.append(text)

    text_list = book_list[indexes_of_names[-1] + 2:]
    text = ""
    for el in text_list:
        text += el
    text_from_chapter_list.append(text)
    return text_from_chapter_list


def frequency_of_words(some_text: str) -> dict:
    frequency_of_words_dict = {}
    list_of_words = some_text.split()
    number_of_all_words = 0
    for word in list_of_words:
        word = word.lower()
        if word not in frequency_of_words_dict:
            frequency_of_words_dict[word] = 1
            number_of_all_words += 1
        else:
            frequency_of_words_dict[word] += 1
            number_of_all_words += 1
    for word in frequency_of_words_dict:
        frequency_of_words_dict[word] = round(frequency_of_words_dict[word] / number_of_all_words, 3)

    return frequency_of_words_dict


def add_file():
    """Makes a .txt file for every chapter. Name of that file is the name of the chapter. Inside the file is text
    from that chapter """
    cnt = 0
    for i in range(num_of_chapters()[0]):
        os.chdir(f"Part_1/CHAPTER_{i+1}")
        with open(f"{name_of_file_list()[0][i]}txt", "w") as n:
            n.write(text_from_chapter()[i])
        with open(f"Analytics_CHAPTER_{i+1}", "w") as a:
            frequency_of_words_dict = frequency_of_words(text_from_chapter()[i])
            for word in frequency_of_words_dict:
                a.write(f"{word} : {frequency_of_words_dict.get(word)}\n")

        cnt = i
        os.chdir("../../")

    for j in range(num_of_chapters()[1]):
        os.chdir(f"Part_2/CHAPTER_{j+1}")
        with open(f"{name_of_file_list()[0][cnt+j+1]}txt", "w") as k:
            if cnt+j+1 < len(text_from_chapter()):
                k.write(text_from_chapter()[cnt+j+1])
        with open(f"Analytics_CHAPTER_{j+1}", "w") as a:
            frequency_of_words_dict = frequency_of_words(text_from_chapter()[cnt+j+1])
            for word in frequency_of_words_dict:
                a.write(f"{word} : {frequency_of_words_dict.get(word)}\n")
        os.chdir("../../")


def make_all_analytics():
    counter = 0
    num_of_words_chapters = {}
    text_chapter = text_from_chapter()
    for i in range(num_of_chapters()[0]):
        list_words = []
        words = text_chapter[i].split()
        for word_ in words:
            word_ = word_.lower()
            if word_ not in list_words:
                list_words.append(words)
        num_of_words_chapters[f"Part_1_CHAPTER_{i+1}"] = len(list_words)
        counter = i

    for j in range(num_of_chapters()[1]):
        list_words = []
        words = text_chapter[counter+j+1].split()
        for word_ in words:
            word_ = word_.lower()
            if word_ not in list_words:
                list_words.append(words)
        num_of_words_chapters[f"Part_2_CHAPTER{counter+j+1}"] = len(list_words)

    sorted_dict = sorted(num_of_words_chapters.items(), key=lambda x: x[1], reverse=True)
    os.mkdir("all_analytics")

    with open("all_analytics/all_analytics.txt", "w") as an:
        for chapter in sorted_dict:
            an.write(f"{chapter[0]} : {chapter[1]}\n")


if __name__ == "__main__":
    with open("20000 leagues-under-Jules-Verne-[ebooksread.com].txt", "r") as f:
        book_list = f.readlines()
    make_part12_folders()
    add_file()
    make_all_analytics()
