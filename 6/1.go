package main

include "/home/owsei/Documents/go/gutil.go"

func main(){ var file FILE
	var err error
	var line string
	var init []string
	var tic int
	var TotalFish int
	const MaxTic = 2
	var sea = map[int]int{
		0:0,
		1:0,
		2:0,
		3:0,
		4:0,
		5:0,
		6:0,
		7:0,
		8:0,
	}
	var OldSea= map[int]int{
		0:0,
		1:0,
		2:0,
		3:0,
		4:0,
		5:0,
		6:0,
		7:0,
		8:0,
	}
	file, err = fopen("i")
	if ( err != nil ) { fprintf(stderr, "can't open file: %s", err) }
	line, err= bufio.NewReader(file).ReadString('\n')
	line = line[:len(line)-1]
	init = split(line, ",")
	file.Close()
	if ( err != nil ) { fprintf(stderr, "can't read file: %s", err) }

	// make starting fish
	for i := 0 ; i < len(init) ; i++ {
		num, err := strconv.Atoi(init[i])
		if ( err != nil ) { fprintf(stderr, "can't convert '%c': %s", init[i], err) }
		printf("%d + %d", sea, num)
		sea[num]++
		printf(" = %d\n", sea)
	}

	// run sim
	for tic = 0 ; MaxTic > tic ; tic++ {
		OldSea[0] = sea[1]
		OldSea[1] = sea[2]
		OldSea[2] = sea[3]
		OldSea[3] = sea[4]
		OldSea[4] = sea[5]
		OldSea[5] = sea[6]
		OldSea[6] = sea[7]+sea[0]
		OldSea[7] = sea[8]
		OldSea[8] = sea[0]
		sea = OldSea
		printf("%d,%d,%d,%d,%d,%d,%d,%d,%d\n", sea[0], sea[1], sea[2], sea[3], sea[4], sea[5], sea[6], sea[7], sea[8])
	}
	for i := 0 ; i < 8 ; i++ {
		TotalFish+=sea[i]
	}
	printf("tf: %d\n", TotalFish)

	exit(0)
}
