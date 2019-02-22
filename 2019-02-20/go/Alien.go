package main

import (
  "fmt"
)

type Alien struct {
  eggsPerDay  int
}

type Egg struct {
  incubationDur int
}

type Nest struct {
  aliens []*Alien
  eggs []*Egg
}


func main() {
  nest := newNest()


  for i := 0; i <= 30; i++ {
    nest.layEggs()
    nest.incubate()
    fmt.Println("Day: ",i,". ", len(nest.aliens), " aliens and ", len(nest.eggs), " eggs")
  }

}

func newNest() (nest *Nest){
  return &Nest{
    aliens: []*Alien{ newAlien() },
  }
}

func (nest *Nest) hatch(egg int){
  nest.eggs = append(nest.eggs[:egg], nest.eggs[egg+1:]...)
  nest.aliens = append(nest.aliens, newAlien());
}

func (nest *Nest) incubate() {
  for i := 0; i < len(nest.eggs); i++ {
    nest.eggs[i].incubationDur--
    if nest.eggs[i].incubationDur == 0{
      nest.hatch(i)
      i-- // decrement i to adjust for removing the current object
    }
  }
}

func (nest *Nest) layEggs() {
  for _, alien := range nest.aliens{
    for i := 0; i < alien.eggsPerDay; i++{
      nest.eggs = append(nest.eggs, newEgg())
    }
  }
}

func newAlien() *Alien {
  return &Alien{ eggsPerDay: 3 }
}

func newEgg() *Egg {
  return &Egg{ incubationDur: 5 }
}
