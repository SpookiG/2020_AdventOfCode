using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

namespace day18
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Running tests:");
            Console.WriteLine("Tests for question 1:");
            string[] testInputs1 = new string[] {"(5 + (5) * 2)", "1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))", "2 * 3 + (4 * 5)", "5 + (8 * 3 + 9 + 3 * 4 * 3)", "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"};
            long[] expectedResults1 = new long[] {20, 71, 51, 26, 437, 12240, 13632};
            long passCount1 = 0;
            foreach ((string input, long expectedResult) in testInputs1.Zip(expectedResults1))
            {
                long testResult = InputHandler.Calculate1(input);
                bool testPass = testResult == expectedResult;
                Console.WriteLine($"Expected result: {expectedResult}. Actual result: {testResult}. Pass?: {testPass}");
                if (testPass)
                {
                    passCount1++;
                }
            }

            bool testPass1 = passCount1 > 0 && passCount1 == expectedResults1.Length; // make sure some tests are run and it doesn't pass just because there are no tests


            Console.WriteLine("Tests for question 2:");
            //string[] testInputs1 = new string[] {"1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))", "2 * 3 + (4 * 5)", "5 + (8 * 3 + 9 + 3 * 4 * 3)", "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"};
            BigInteger[] expectedResults2 = new BigInteger[] {new BigInteger(20), new BigInteger(231), new BigInteger(51), new BigInteger(46), new BigInteger(1445), new BigInteger(669060), new BigInteger(23340)};
            long passCount2 = 0;
            foreach ((string input, BigInteger expectedResult) in testInputs1.Zip(expectedResults2))
            {
                BigInteger testResult = InputHandler.Calculate2(input);
                bool testPass = testResult == expectedResult;
                Console.WriteLine($"Expected result: {expectedResult}. Actual result: {testResult}. Pass?: {testPass}");
                if (testPass)
                {
                    passCount2++;
                }
            }

            bool testPass2 = passCount2 > 0 && passCount2 == expectedResults2.Length; // make sure some tests are run and it doesn't pass just because there are no tests
            

            if (testPass1)
            {
                Console.WriteLine("\n\nTest 1 passed! Parsing input 1:");
                List<long> results = new List<long>();

                using (StreamReader reader = new StreamReader(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\input.txt"))
                {
                    while (reader.Peek() > -1)
                    {
                        results.Add(InputHandler.Calculate1(reader.ReadLine()));
                    }
                }

                long resultSum = results.Sum();
                Console.WriteLine($"Sum of results: {resultSum}");
            }

            if (testPass2)
            {
                Console.WriteLine("\n\nTest 2 passed! Parsing input 2:");
                List<BigInteger> results = new List<BigInteger>();

                using (StreamReader reader = new StreamReader(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\input.txt"))
                {
                    while (reader.Peek() > -1)
                    {
                        results.Add(InputHandler.Calculate2(reader.ReadLine()));
                    }
                }

                BigInteger total = 0;
                foreach (BigInteger r in results)
                {
                    total += r;
                    //Console.WriteLine($"result: {r} | total: {total}");
                }

                //long resultSum = results.Sum();
                Console.WriteLine($"Sum of results: {total}");
            }
        }
    }

    public static class InputHandler
    {
        //private readonly long[] longs = {"0", } 

        public static long Calculate1(string expression)
        {
            Stack<long> results = new Stack<long>();
            Stack<char> operations = new Stack<char>();
            string num = "";

            results.Push(0);
            operations.Push('+');

            foreach (char c in expression.Trim())
            {
                if (c == '(')
                {
                    results.Push(0);
                    operations.Push('+');
                }

                if (c == ')')
                {
                    // assuming every bracket closes on a number or another ) because otherwise the expression doesn't make sense
                    if (num != "")
                    {
                        results.Push(long.Parse(num));
                        num = "";

                        results.Push(RunOperation(results, operations));
                    }
                    
                    results.Push(RunOperation(results, operations));
                }

                if (c == '+' || c == '-' || c == '*')
                {
                    operations.Push(c);
                }
               
                if (c == ' ' && num != "")
                {
                    results.Push(long.Parse(num));
                    num = "";

                    results.Push(RunOperation(results, operations));
                }

                if (Char.IsNumber(c))
                {
                    num += c;
                }

            }

            if (num != "")
            {
                results.Push(long.Parse(num));
                results.Push(RunOperation(results, operations));
            }



            return results.Pop();
        }

        private static long RunOperation(Stack<long> results, Stack<char> operations)
        {
            // stack is popped in reverse order so b first
            long b = results.Pop();
            long a = results.Pop();
            char operation = operations.Pop();

            if (operation == '+')
            {
                return a + b;
            }

            if (operation == '-')           // oops there is not - operator, I just assumed there was oops
            {
                return a - b;
            }

            // by deduction, the only other possible operation is *
            return a * b;
        }

        // question 2 involves numbers that get so large that even longs are wrapping, had to replace all longs with BigIntegers, which also prevented RunOperation() from being reused when the same functionality is needed
        public static BigInteger Calculate2(string expression)
        {
            Stack<Stack<BigInteger>> resultsPerBracket = new Stack<Stack<BigInteger>>();
            Stack<Stack<char>> operationsPerBracket = new Stack<Stack<char>>();
            string num = "";

            // a little awkward but this makes sure the CompleteBracketOperations() function has something to add to once the whole final expression's result is calculated
            resultsPerBracket.Push(new Stack<BigInteger>());
            resultsPerBracket.Peek().Push(0);
            resultsPerBracket.Push(new Stack<BigInteger>());
            resultsPerBracket.Peek().Push(0);
            operationsPerBracket.Push(new Stack<char>());
            operationsPerBracket.Peek().Push('+');

            foreach (char c in expression.Trim())
            {
                if (c == '(')
                {
                    resultsPerBracket.Push(new Stack<BigInteger>());
                    operationsPerBracket.Push(new Stack<char>());
                    resultsPerBracket.Peek().Push(0);
                    operationsPerBracket.Peek().Push('+');
                }

                if (c == ')')
                {
                    // assuming every bracket closes on a number or another ) because otherwise the expression doesn't make sense
                    if (num != "")
                    {
                        resultsPerBracket.Peek().Push(new BigInteger(long.Parse(num)));
                        num = "";

                        // if plus run operation now
                        if (operationsPerBracket.Peek().Peek() == '+')
                        {
                            resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));
                        }
                    }
                    
                    // run all inner bracket operations & pop bracket stack
                    CompleteBracketOperations(resultsPerBracket, operationsPerBracket);

                    // if there was a + before the bracket, we need to add the bracket result now
                    if (operationsPerBracket.Peek().Peek() == '+')
                    {
                        resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));
                    }
                }

                if (c == '+' || c == '-' || c == '*')
                {
                    operationsPerBracket.Peek().Push(c);
                }
               
                if (c == ' ' && num != "")
                {
                    resultsPerBracket.Peek().Push(new BigInteger(long.Parse(num)));
                    num = "";

                    // if plus run operation now
                    if (operationsPerBracket.Peek().Peek() == '+')
                    {
                        resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));
                    }
                    
                }

                if (Char.IsNumber(c))
                {
                    num += c;
                }

            }

            if (num != "")
            {
                resultsPerBracket.Peek().Push(new BigInteger(long.Parse(num)));
                num = "";

                // if plus run operation now
                if (operationsPerBracket.Peek().Peek() == '+')
                {
                    resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));
                }
            }

            
                    
            // run all inner bracket operations & pop bracket stack
            CompleteBracketOperations(resultsPerBracket, operationsPerBracket);

            //resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));

            BigInteger result = resultsPerBracket.Peek().Pop();
            //Console.WriteLine($"Bracket stack size {resultsPerBracket.Count} | Internal Bracket stack size {resultsPerBracket.Peek().Count}");

            
            return result;
        }


        private static void CompleteBracketOperations(Stack<Stack<BigInteger>> resultsPerBracket, Stack<Stack<char>> operationsPerBracket)
        {
            while (operationsPerBracket.Peek().Count > 0)
            {
                resultsPerBracket.Peek().Push(RunOperationBig(resultsPerBracket.Peek(), operationsPerBracket.Peek()));
            }

            BigInteger bracketResult = resultsPerBracket.Peek().Pop();
            resultsPerBracket.Pop();
            operationsPerBracket.Pop();
            resultsPerBracket.Peek().Push(bracketResult);
        }

        // RunOperationBig is a functional copy of RunOperation, just for BigIntegers because the 2nd question uses large numbers
        private static BigInteger RunOperationBig(Stack<BigInteger> results, Stack<char> operations)
        {
            // stack is popped in reverse order so b first
            BigInteger b = results.Pop();
            BigInteger a = results.Pop();
            char operation = operations.Pop();

            if (operation == '+')
            {
                return a + b;
            }

            if (operation == '-')           // oops there is not - operator, I just assumed there was oops
            {
                return a - b;
            }

            // by deduction, the only other possible operation is *
            return a * b;
        }
    }
}
