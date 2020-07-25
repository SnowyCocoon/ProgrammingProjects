/*
 * Player.h
 *
 *  Created on: 2018 M08 7
 *      Author: Dominik Strzałko
 */

#ifndef PLAYER_H_
#define PLAYER_H_
#include <iostream>

class Player {
	public:
			Player(std::string,std::string,int,int);
			void LevelUp();
			void CheckStats();
			void DrinkPotion();
			void TestSelfharm();
			void TestFreeExp();
			void InstaLevelUp();
			int SaveHero();

			void setName(std::string name) {HeroName = name;}
		    void setLocation(std::string location) {HeroLocation = location;}
		    void setLvl(int lvl) {HeroLvl = lvl;}
		    void setExp(int exp) {HeroExp = exp;}
		    void setHP(double hp) {HeroHP = hp;}
		    void setMaxHP() {HeroMaxHP = 100 + (getLvl() * 50);}
		    void setStrength() {HeroStrength = 5 + (getLvl() *2);}
		    void setExpReq() {HeroExpReq = 90 + (getLvl() * getLvl() * 15);}
		    void setGold(int gold) {HeroGold = gold;}


		    std::string getName() {return HeroName;}
		    std::string getLocation() const {return HeroLocation;}
		    int getLvl() const {return HeroLvl;}
		    int getExp() {return HeroLvl;}
		    double getHP() {return HeroHP;}
		    double getMaxHP() {return HeroMaxHP;}
		    int getStrength() {return HeroStrength;}
		    int getExpReq() {return HeroExpReq;}
		    int getGold() {return HeroGold;}


	private:
			std::string HeroName;
		    std::string HeroLocation;
		    int HeroLvl;
		    double HeroHP;
		    double HeroMaxHP;
		    int HeroStrength;
		    int HeroExp;
		    int HeroExpReq;
		    int HeroGold;
	};

#endif /* PLAYER_H_ */
