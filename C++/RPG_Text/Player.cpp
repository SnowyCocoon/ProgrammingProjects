/*
 * Player.cpp
 *
 *  Created on: 2018 M08 7
 *      Author: Dominik Strzałko
 */
#include <string>
#include "Player.h"
#include <fstream>

Player::Player(std::string name,std::string location,int level,int exp) {
		setName(name);
		setLocation(location);
		setLvl(level);
		setExp(exp);
		setMaxHP();
		setHP(HeroMaxHP);
		setStrength();
		setGold(10);
		setExpReq();
}

void Player::InstaLevelUp(){
	HeroExp = HeroExpReq;
	LevelUp();

}


int Player::SaveHero(){

	std::ofstream savefile("mysavedgame.txt");
	if (!savefile)
	{
		std::cout << "Sorry: there was a problem, and I couldn't save your game!" << std::endl;
		return -1;
	}

	savefile << HeroName << "\n"
		<< HeroLocation << "\n"
		<< HeroLvl << "\n"
		<< HeroExp << "\n"
		<< HeroHP << "\n"
		<< HeroGold << "\n"				
		<< std::endl;
	savefile.close();

	std::cout << "Game Saved! \n\n";

	return 0;	
}

void Player::LevelUp(){
	while(HeroExp >= HeroExpReq)
	{
	HeroExp -= HeroExpReq;
	HeroLvl++;
	setMaxHP();
	setStrength();
	setExpReq();
	setHP(getMaxHP());
	std::cout << "Congratz! you are now level " << HeroLvl << "! \n\n";
	}
}

void Player::CheckStats(){
	std::cout << "Your Name: " << HeroName << std::endl;
	std::cout << "Your Location: " << HeroLocation << std::endl;
	std::cout << "Your Level: " << HeroLvl << std::endl;
	std::cout << "Exp till next Level: " << HeroExpReq-HeroExp << std::endl;
	std::cout << "Your Hitpoints: " << HeroHP << "/" << HeroMaxHP << std::endl;
	std::cout << "Your Strength: " << HeroStrength << std::endl;
	std::cout << "Your Gold: " << HeroGold << std::endl << std::endl;
}




void Player::DrinkPotion(){
	if (HeroGold >= 5 && HeroHP < 150 )
	{
		HeroGold -= 5;
		HeroHP += 10;
		if(HeroHP > HeroMaxHP)
		{
			HeroHP = HeroMaxHP;
			std::cout << "You have max HP now. \n";
		}
		std::cout << "You bought and drank a potion. you HP is now" << HeroHP << "/" << HeroMaxHP <<"." << std::endl << std::endl;
	}
	else if(HeroHP == HeroMaxHP)
	{
		std::cout << " You have full hp. You don't have to buy potions! \n\n";
	}
	else
	{
		std::cout << "You don't have enough gold. You need " << HeroGold << "more. Come back later." << std::endl << std::endl;
	}
}

void Player::TestSelfharm(){
	std::cout << "Ouch! -10 Hp. \n\n";
	HeroHP -= 10;
}

void Player::TestFreeExp(){
	std::cout << "Free 50 exp! \n\n";
	HeroExp += 50;
}
