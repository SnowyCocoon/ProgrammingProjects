//============================================================================
// Name          : TextRpg.cpp
// Author        : Dominik Strzałko
// Version       : 1.0.0
// Copyright     : Your copyright notice
// Description   : Text RPG(like) game
// Creation Date : 7.08.2018
//============================================================================

#include "Player.h"
#include "Enemy.h"
#include <string>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>

int Load=0;


Player fight(Player Hero) //Repair in progress
{
	std::cout << "Fight Demo with random monster \n";
	std::string Enemies[4][2] = { {"Spider","Goblin"},{"Ice Warrior","Chaos Druid"},{"Ankou","Revenant"},{"Calisto","Vet'ion"}};
	srand(time(0));
	int RandomEnemy = (rand() % 2);
	int RandomType = (rand() % 4);
	Enemy Monster(Enemies[RandomType][RandomEnemy], Hero.getLvl(), RandomType + 1);

	Monster.CheckStats();
	int MaxHP = Monster.getHP();
	int Flee;


	while (Monster.getHP() > 0 && Hero.getHP() > 0)
	{
		std::cout << "Your HP is now: " << Hero.getHP() << "	Monster HP is now: "<< Monster.getHP() << "\n\n";
		std::cout << "What do you want to do?\n";
		std::cout << "1. Attack \n";
		std::cout << "2. Try to run away\n";

		int choice;
		std::cin >> choice;
		std::cout << std::endl;

		switch (choice)
		{
		case 1: {
			int HeroHit = Hero.getStrength() * (rand() % 3);
			Monster.setHP(Monster.getHP() - HeroHit);
			std::cout << "You hit Monster for: "<< HeroHit <<" hp\n\n";

			int MonsterHit = Monster.getStrength() * (rand() % 2);
			Hero.setHP(Hero.getHP() - MonsterHit);
			std::cout << "Monster hit you for: "<< MonsterHit <<"hp\n";			
			break;}
		case 2: {
			int Flee = (rand() % 9);
			if (Flee >= 5)
			{
				std::cout << "You ran away from danger\n";
				return Hero;
			}
			else
			{
				std::cout << "Escape Failed\n";
				int MonsterHit = Monster.getStrength() * (rand() % 2);
				Hero.setHP(Hero.getHP() - MonsterHit);
				std::cout << "Monster hit you for: " << MonsterHit << "hp\n";
			}
			break;}
		default:
			std::cout << "Your choice is invalid.\n\n";
		}

	}
	if (Monster.getHP() <= 0)
	{
		int ExpGained = Hero.getExp() + ((MaxHP / 2) * Monster.getDifficulty());
		std::cout << "Victory. You've gained: " << ExpGained - Hero.getExp() << " Exp. Returning to the village. \n\n";		
		Hero.setExp(Hero.getExp() + ExpGained);
		return Hero;
	}
	if (Hero.getHP() <= 0)
	{
		return Hero;
	}
}

Player LoadGame(Player Hero){

	std::ifstream loadfile("mysavedgame.txt");

	if (!loadfile)
	{
		std::cout << "Error! Cannot load game. You have to start from the beggining" << std::endl;
		return Hero;
	}

	std::string temporaryString;

	//When you load data with getline we are placing it into a std::string
	//However, you want some of you data to go into and int right?
	//So we use atoi(...) to convert it to an int for us.


	getline(loadfile, temporaryString);
	Hero.setName(temporaryString);

	getline(loadfile, temporaryString);
	Hero.setLocation(temporaryString);

	getline(loadfile, temporaryString);
	Hero.setLvl(atoi(temporaryString.c_str()));

	getline(loadfile, temporaryString);
	Hero.setExp(atoi(temporaryString.c_str()));

	getline(loadfile, temporaryString);
	Hero.setHP(atoi(temporaryString.c_str()));

	getline(loadfile, temporaryString);
	Hero.setGold(atoi(temporaryString.c_str())) ;

	loadfile.close();

	
	return Hero;
}


void Game(){

		std::string Name = "anon";
		std::string Location = "Seaside";
		Player Hero(Name, Location, 1, 0);

	if (Load == 1)
		{		
		Hero = LoadGame(Hero);
		std::cout << "Game loaded! \n\n";
		}
		else
		{
		std::cout << "Welcome to my RPG Demo. please enter your name. \n";
		std::string Name;
		std::cin >> Name;
		Hero.setName(Name);
		std::cout << "Welcome " << Hero.getName() << " Your adventure begins right here. See You later \n\n";
		}
		
		//main loop
		while(Hero.getHP() > 0)
		{
			Hero.LevelUp();

			std::cout << "## Welcome in Menu. What do you want to do? ## \n";
			std::cout << "0. Move \n";
			std::cout << "1. Check your stats \n";
			std::cout << "2. Go fight \n";
			std::cout << "3. Buy potion in a Shop \n";
			std::cout << "4. (test) Instant lvl up  \n";
			std::cout << "5. (test) -10 hp \n";
			std::cout << "6. (test) Free Exp \n";
			std::cout << "7. (test) Clear the screen \n";
			std::cout << "8. Save the game \n";
			std::cout << "9. Save and quit \n";
			std::cout << "10. Quit \n";
			int MenuInt;
			std::cin >> MenuInt;
			std::cout << std::endl;

			switch(MenuInt)
			{
			case 0:
					int move;
					std::cout << "Type 1 to move forward, 2 to move backward, 3/4 to move left/right \n";
					std::cout << "  1  \n";
					std::cout << "3   4   Your move: ";
					std::cin >> move;
					std::cout << "  2  \n\n";
					std::cout << "you've chosen: " << move <<" and something want to fight!\n\n";
					break;
			case 1: //Stats
					Hero.CheckStats();
					break;
			case 2: //Stats
					Hero = fight(Hero);
					break;
			case 3: //Potion
					Hero.DrinkPotion();
					break;
			case 4: //LevelUp
					Hero.InstaLevelUp();
					break;
			case 5: //Stats
					Hero.TestSelfharm();
					break;
			case 6: //Stats
					Hero.TestFreeExp();
					break;
			case 7: //Stats
					break;
			case 8: //Stats
					Hero.SaveHero();
					break;
			case 9:
					Hero.SaveHero();
					exit(0);
					break;
			case 10:
					exit(0);
					break;
			default:
			         std::cout << "Your choice is invalid.\n\n";
			}
		}
		if(Hero.getHP() <= 0)
		{
			std::cout << "You're dead. See you next time! \n\n";
		}
}




int main() {
	while(1){
	std::cout << "The art of gamedev\n";
	std::cout << "1. New Game\n";
	std::cout << "2. Load Game\n";
	std::cout << "3. Quit\n";
	int choice;
	std::cin>>choice;

	switch(choice)
	{
	case 1: //New Game
			Game();
			break;
	case 2: //Load game
			Load = 1;
			Game();
			break;
	case 3: //quit
			return 0;
			break;
	default:
			std::cout<<"Please pick from 1 to 3 \n\n";
	}
	} // the end of main menu loop

}
