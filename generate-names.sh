rm -f char-rnn-tensorflow/save/*
rm -f char-rnn-tensorflow/dataset/*

docker stop namegen
docker build -t namegen .
docker run -it --rm -v ${PWD}:/namegen --name namegen -d namegen 
docker exec -it namegen sh -c "python3 generate.py --page '${1}'" 
cat results.txt
rm results.txt

