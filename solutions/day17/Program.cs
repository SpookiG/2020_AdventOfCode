using System;
using System.IO;
using System.Collections.Generic;

namespace day17
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Parsing inputs:");
            Console.WriteLine(AppDomain.CurrentDomain.BaseDirectory);
            HashSet<Vector3> Test1Input = InputHandler.Parse1(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\test1input.txt");
            HashSet<Vector4> Test2Input = InputHandler.Parse2(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\test1input.txt");

            HashSet<Vector3> Input1 = InputHandler.Parse1(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\input.txt");
            HashSet<Vector4> Input2 = InputHandler.Parse2(AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\input.txt");
            Console.WriteLine("Inputs parsed");


            Console.WriteLine("\nRunning tests:");
            int expectedResult1 = 112;
            int expectedResult2 = 848;

            Console.WriteLine("Running test 1:");
            int test1Result = Solver.RunProblem1(Test1Input);
            bool test1Pass = test1Result == expectedResult1;
            Console.WriteLine($"Expected result: {expectedResult1}. Actual result: {test1Result}. Pass?: {test1Pass}");

            Console.WriteLine("Running test 2:");
            int test2Result = Solver.RunProblem2(Test2Input);
            bool test2Pass = test2Result == expectedResult2;
            Console.WriteLine($"Expected result: {expectedResult2}. Actual result: {test2Result}. Pass?: {test2Pass}");
            



            if (test1Pass)
            {
                Console.WriteLine("\n\nTest 1 passed! Running input 1:");
                int result1 = Solver.RunProblem1(Input1);
                Console.WriteLine($"Result: {result1}");
            }

            if (test2Pass)
            {
                Console.WriteLine("\n\nTest 1 passed! Running input 1:");
                int result2 = Solver.RunProblem2(Input2);
                Console.WriteLine($"Result: {result2}");
            }
        }
    }
   


    public static class InputHandler
    {
        public static HashSet<Vector3> Parse1(string fileLocation)
        {
            HashSet<Vector3> cubes = new HashSet<Vector3>();
            int y = 0;

            using (StreamReader reader = new StreamReader(fileLocation))
            {
                while (reader.Peek() > -1)
                {
                    string line = reader.ReadLine();
                    int x = 0;
                    foreach (char c in line)
                    {
                        if (c == '#')
                        {
                            cubes.Add(new Vector3(x, y, 0));
                        }
                        x++;
                    }
                    y++;
                }
            }

            return cubes;
        }

        public static HashSet<Vector4> Parse2(string fileLocation)
        {
            HashSet<Vector4> cubes = new HashSet<Vector4>();
            int y = 0;

            using (StreamReader reader = new StreamReader(fileLocation))
            {
                while (reader.Peek() > -1)
                {
                    string line = reader.ReadLine();
                    int x = 0;
                    foreach (char c in line)
                    {
                        if (c == '#')
                        {
                            cubes.Add(new Vector4(x, y, 0, 0));
                        }
                        x++;
                    }
                    y++;
                }
            }

            return cubes;
        }
    }

    public static class Solver
    {
        public static int RunProblem1(HashSet<Vector3> cubes)
        {
            for (int i = 0; i < 6; i++)
            {
                Dictionary<Vector3, int> neighbours = GenerateNeighbourCount1(cubes);
                cubes = GenerateNewCubePositions1(cubes, neighbours);
                
            }

            return cubes.Count;
        }

        public static int RunProblem2(HashSet<Vector4> cubes)
        {
            for (int i = 0; i < 6; i++)
            {
                Dictionary<Vector4, int> neighbours = GenerateNeighbourCount2(cubes);
                cubes = GenerateNewCubePositions2(cubes, neighbours);
                
            }

            return cubes.Count;
        } 


        private static Dictionary<Vector3, int> GenerateNeighbourCount1(HashSet<Vector3> cubes)
        {
            Dictionary<Vector3, int> neighbours = new Dictionary<Vector3, int>();

            foreach (Vector3 cube in cubes)
            {
                for (int x = cube.X-1; x <= cube.X+1; x++)
                {
                    for (int y = cube.Y-1; y <= cube.Y+1; y++)
                    {
                        for (int z = cube.Z-1; z <= cube.Z+1; z++)
                        {
                            // don't count cube as it's own neighbour
                            if (x != cube.X || y != cube.Y || z != cube.Z)
                            {
                                if (neighbours.ContainsKey(new Vector3(x, y, z)))
                                {
                                    neighbours[new Vector3(x, y, z)] += 1;
                                }
                                else
                                {
                                    neighbours[new Vector3(x, y, z)] = 1;
                                }
                            }
                        }
                    }
                }
            }

            return neighbours;
        }

        private static HashSet<Vector3> GenerateNewCubePositions1(HashSet<Vector3> cubes, Dictionary<Vector3, int> neighbours)
        {
            HashSet<Vector3> newCubes = new HashSet<Vector3>();

            // This will skip over cubes with no neighbours but by the logic of the rules these cubes become inactive and so are not added to the newCubes HashSet anyway 
            foreach (Vector3 position in neighbours.Keys)
            {
                // rule 1: active cube with 2-3 neighbours remains active
                if (cubes.Contains(position))
                {
                    if (neighbours[position] == 2 || neighbours[position] == 3)
                    {
                        newCubes.Add(position);
                    }
                }

                // rule 2: inactive cube with exactly 3 neighbours becomes active
                else
                {
                    if (neighbours[position] == 3)
                    {
                        newCubes.Add(position);
                    }
                }
            }

            return newCubes;
        }







        private static Dictionary<Vector4, int> GenerateNeighbourCount2(HashSet<Vector4> cubes)
        {
            Dictionary<Vector4, int> neighbours = new Dictionary<Vector4, int>();

            foreach (Vector4 cube in cubes)
            {
                for (int x = cube.X-1; x <= cube.X+1; x++)
                {
                    for (int y = cube.Y-1; y <= cube.Y+1; y++)
                    {
                        for (int z = cube.Z-1; z <= cube.Z+1; z++)
                        {
                            for (int w = cube.W-1; w <= cube.W+1; w++)
                            {
                                // don't count cube as it's own neighbour
                                if (x != cube.X || y != cube.Y || z != cube.Z || w != cube.W)
                                {
                                    if (neighbours.ContainsKey(new Vector4(x, y, z, w)))
                                    {
                                        neighbours[new Vector4(x, y, z, w)] += 1;
                                    }
                                    else
                                    {
                                        neighbours[new Vector4(x, y, z, w)] = 1;
                                    }
                                }
                            }
                            
                        }
                    }
                }
            }

            return neighbours;
        }

        private static HashSet<Vector4> GenerateNewCubePositions2(HashSet<Vector4> cubes, Dictionary<Vector4, int> neighbours)
        {
            HashSet<Vector4> newCubes = new HashSet<Vector4>();

            // This will skip over cubes with no neighbours but by the logic of the rules these cubes become inactive and so are not added to the newCubes HashSet anyway 
            foreach (Vector4 position in neighbours.Keys)
            {
                // rule 1: active cube with 2-3 neighbours remains active
                if (cubes.Contains(position))
                {
                    if (neighbours[position] == 2 || neighbours[position] == 3)
                    {
                        newCubes.Add(position);
                    }
                }

                // rule 2: inactive cube with exactly 3 neighbours becomes active
                else
                {
                    if (neighbours[position] == 3)
                    {
                        newCubes.Add(position);
                    }
                }
            }

            return newCubes;
        }




    }

    // Vector3 is a struct so it can be indexed by value in a dictionary
    public struct Vector3
    {
        public Vector3(int x, int y, int z)
        {
            X = x;
            Y = y;
            Z = z;
        }

        public int X;
        public int Y;
        public int Z;

        public override string ToString()
        {
            return $"({X}, {Y}, {Z})";
        }
    }


    // question 2 simply requires rearranging for 4d vectors
    public struct Vector4
    {
        public Vector4(int x, int y, int z, int w)
        {
            X = x;
            Y = y;
            Z = z;
            W = w;
        }

        public int X;
        public int Y;
        public int Z;
        public int W;

        public override string ToString()
        {
            return $"({X}, {Y}, {Z}, {W})";
        }
    }
}
