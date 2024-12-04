import Data.List
import System.IO

-- From here to the closing comment is stolen is stolen cod from SO
import Control.Applicative
import Data.Traversable (sequenceA)
import Data.List (tails)


transpose' :: [[a]] -> [[a]]
transpose' = getZipList . sequenceA . map ZipList

windows :: [a] -> [[a]]
windows = transpose' . take 3 . tails

diagonals :: [String] -> [String]
diagonals []       = []
diagonals ([]:xss) = xss
diagonals xss      = zipWith (++) (map ((:[]) . head) xss ++ repeat [])
                                  ([]:(diagonals (map tail xss)))
-- closing comment

part1 :: String -> Int
part1 input = (hor_ input) + (vert_ input) + (diags_ input)

hor_ :: String -> Int
hor_ input = hor input + (hor $ reverse input)

hor (a:b:c:d:ls) = if [a,b,c,d]=="XMAS" then 1+hor n else hor n
  where n = b:c:d:ls
hor _ = 0

vert_ = sum . map hor_ . transpose . lines

diags_ i = (sum . map hor_ . diagonals $ lines i) + (sum . map hor_ . diagonals . reverse $ lines i)

part2 :: String -> Int
part2 input = (sum $ map count parsed)
 where parsed = map (concat . transpose) . windows . map windows . lines $ input 

count ((a1:_:a2:_):(_:b:_):(c1:_:c2:_):others) = count others + if
  (f == "MAS" && s == "MAS") || (f == "SAM" && s == "SAM") || (f == "MAS" && s == "SAM") || (f == "SAM" && s == "MAS") then 1 else 0
  where f = [a1,b,c2]
        s = [c1,b,a2]
count _ = 0

main = hGetContents stdin >>= pure . part2  >>= print
