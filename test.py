def analyze_text(text):
    """分析文本内容，返回单词数量、句子数量和最长单词"""
    if not text.strip():
        return {
            'word_count': 0,
            'sentence_count': 0,
            'longest_word': ''
        }
    
    # 统计句子数量（简单以句号、问号、感叹号作为句子结束标志）
    sentence_count = len([c for c in text if c in '.?!'])
    
    # 处理文本，提取单词
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    cleaned_text = text.translate(str.maketrans('', '', punctuation))
    words = cleaned_text.lower().split()
    
    # 统计单词数量
    word_count = len(words)
    
    # 找到最长单词
    longest_word = max(words, key=len) if words else ''
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'longest_word': longest_word
    }

def main():
    print("文本分析工具")
    print("-" * 20)
    
    # 获取用户输入
    user_text = input("请输入要分析的文本: ")
    
    # 分析文本
    result = analyze_text(user_text)
    
    # 显示结果
    print("\n分析结果:")
    print(f"单词数量: {result['word_count']}")
    print(f"句子数量: {result['sentence_count']}")
    print(f"最长单词: {result['longest_word']} (长度: {len(result['longest_word'])})")

if __name__ == "__main__":
    main()
