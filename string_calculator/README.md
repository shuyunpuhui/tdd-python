### String Calculator

The following is a TDD Kata- an exercise in coding, refactoring and test-first, that you should apply daily for at least 15 minutes (I do 30).

#### Before you start:

    - Try not to read ahead.
    - Do one task at a time. The trick is to learn to work incrementally.
    - Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata

#### String Calculator

#### 1 
    创建一个简单的 String calculator，方法定义为 int add(string numbers)
        - 这个方法接受 0, 1 或者 2 数字, 并且返回它们的和 (对于空字符串，返回 0)，输入示例： “” or “1” or “1,2”
        - 从空字符串开始，然后实现1个和2个数字的情况
        - 尽量用最简单的方式来实现，强迫自己考虑测试所有情况
        - 别忘了重构
####2 
    
    允许输入多个数字，例如“1，2，3，4，5”
####3 
    允许换行作为分隔符
        - 这种格式是合法的:  “1\n2,3”  (结果是 6)
        - 这种格式是非法的:  “1,\n” (不需要实现，假设输入不会出现这种情况)
        - 支持自定义分隔符
        - 要定义一个分隔符, 在开始第一行这么写:   “//[delimiter]\n[numbers…]” 例如 “//;\n1;2” 的结果是3
        - 第一行是可选的. 之前的情况依然有效
####4 
    如果输入有负数，则抛出异常并提示 “negatives not allowed” 
    - 并且显示这个数字.
    - 如果有多个负数，则显示所有负数

###### Continue if you can finish the steps so far in less than 30 minutes.
    - Numbers bigger than 1000 should be ignored, so adding 2 + 1001  = 2
    - Delimiters can be of any length with the following format:  “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6
    - Allow multiple delimiters like this:  “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.
    - make sure you can also handle multiple delimiters with length longer than one char
