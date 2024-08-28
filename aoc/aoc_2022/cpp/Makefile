# CC=g++
CC=mpic++
SRC=src
BUILD=build
CFLAGS  = -g -Wall
IFLAGS = -I./include/

source_files := $(wildcard $(SRC)/*.cpp)
all_programs := $(source_files:src/%.cpp=$(BUILD)/%.x)

.PHONY: all
all: $(all_programs)

.PHONY: clean
clean:
	rm -f $(all_programs)

$(BUILD)/%.x: $(SRC)/%.cpp 
	$(CC) $(IFLAGS) $(CFLAGS) $< -o $@
