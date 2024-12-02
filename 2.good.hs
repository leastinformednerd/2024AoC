import System.IO

count :: [a] -> Int
count = sum . map (const 1)

part1 :: [[Int]] -> Int
part1 = count . filter (solve1 0)

solve1 :: Int -> [Int] -> Bool
solve1 dir (dist:dists) = let d = abs(dist) in
  if d < 1 || d > 3 || (dir /= 0 && signum dist /= dir) then False
  else solve1 (signum dist) dists
solve1 _ [] = True

part2 :: [[Int]] -> Int
part2 = count . filter (solve2 True 0)

solve2 :: Bool -> Int -> [Int] -> Bool
solve2 allowed dir (dist:dists) = let d = abs(dist) in
  if d < 1 || d > 3 || (dir /= 0 && signum dist /= dir) then if allowed then solve2 False dir dists else False
  else solve2 allowed (signum dist) dists
solve2 _ _ [] = True
  
parseInp :: String -> [[Int]]
parseInp = map (map read . words) . lines

distance :: [Int] -> [Int]
distance (a:b:abs) = (a-b): distance (b:abs)
distance (a:_) = []

main = do
  inp <- hGetContents stdin
  let parse = parseInp inp
  let dists = map distance parse
  print $ part1 dists
  print $ part2 dists
