import * as mongoose from 'mongoose';

//Benutzer

export interface ILightColors extends mongoose.Document{//Beleuchtungsparameter der Lampen
	amber: number; 
	farRed: number; 
	hyperRed: number; 
	blue: number; 
	red: number; 
	green: number;
	uv: number;
	deepBlue: number;
	white: number;	
};

var SLightColors = new mongoose.Schema({
	amber: Number, 
	farRed: Number, 
	hyperRed: Number, 
	blue: Number, 
	red: Number, 
	green: Number,
	uv: Number,
	deepBlue: Number,
	white: Number
});

export var LightColors = mongoose.model<ILightColors>('LightColors', SLightColors);

export interface IUserProfile extends mongoose.Document{//Systemkonfiguration des Benutzer
	foodQuantity: number; //Drehdauer des Futterautomaten
	foodInterval: number; //Anzahl der Fütterungen pro Tag
	exposureTime: number; //Beleuchtungsdauer der Pflanzen
	exposureInterval: number; //Beleuchtungsintervall
	exposureParameters: ILightColors[]; //Beleuchtungsparameter (Farben)
	waterTemp: number; //Wassertemperatur
	autoRegulation: boolean; //Automatische Regulierung der Wassertemperatur
};

var SUserProfile = new mongoose.Schema({
	foodQuantity: Number, 
	foodInterval: Number,
	exposureTime: Number, 
	exposureInterval: Number, 
	exposureParameters: [SLightColors],
	waterTemp: Number,
	autoRegulation: Boolean
});

export var UserProfile = mongoose.model<IUserProfile>('UserProfile', SUserProfile);

export interface IAccount extends mongoose.Document{
  username: string;
  password: string;
  email: string;
  firstName: string;
  lastName: string;
  systemConfig: IUserProfile[];
};

var SAccount = new mongoose.Schema({
  username: String,
  password: String,
  email: String,
  firstName: String,
  lastName: String,
  systemConfig: [SUserProfile]
});

export var Account = mongoose.model<IAccount>('Account', SAccount);

//--------------------------------------------------------------------------------

//Fische

export interface IFish extends mongoose.Document{
	name: string; //Bezeichnung
	minNumberOfFish: number; //Mindestanzahl von Tieren
	plants: string; //Pflanzen
	planting: string; //Bepflanzung
	origin: string; //Herkunft
	picture: string;
	specialRequirements: string; //Besondere Anforderungen
	food: string;
	waterTemp: string;
	reachableAge: number; //Erreichbares Alter
	pH: number; //pH-Wert
	speciesPool: string; //Benötigt Artenbecken (Ja/Nein)
};

var SFish = new mongoose.Schema({
	name: String,
	minNumberOfFish: Number,
	plants: String,
	planting: String,
	origin: String,
	picture: String,
	specialRequirements: String,
	food: String,
	waterTemp: String,
	reachableAge: Number,
	pH: Number,
	speciesPool: String
});

export var Fish = mongoose.model<IFish>('Fish', SFish);

//--------------------------------------------------------------------------

//Pflanzen

export interface ICharacteristics extends mongoose.Document{
	name: string; //Bezeichnung
	cropDuration: number; //Ernte Dauer
	specialRequirements: string; //Besondere Anforderungen
};

var SCharacteristics = new mongoose.Schema({
	name: String,
	cropDuration: Number,
	specialRequirements: String,
});

export var Characteristics = mongoose.model<ICharacteristics>('Characteristics', SCharacteristics);

export interface IPlant extends mongoose.Document{
	vegetables: ICharacteristics[];
	fruits: ICharacteristics[];
	herbage: ICharacteristics[]; 
};

var SPlant = new mongoose.Schema({
	vegetables:[SCharacteristics],
	fruits: [SCharacteristics],
	herbage: [SCharacteristics] 
});

export var Plant = mongoose.model<IPlant>('Plant', SPlant);

//--------------------------------------------------------------------------------------

//Vordefinierte Profile für Fische und Pflanzen

export interface IPlantSettings extends mongoose.Document{
	exposureTime: number;
	exposureInterval: number;
	exposureParameters: ILightColors[];
};

var SPlantSettings = new mongoose.Schema({
	exposureTime: Number,
	exposureInterval: Number,
	exposureParameters: [SLightColors]
});

export var PlantSettings = mongoose.model<IPlantSettings>('PlantSettings', SPlantSettings);

export interface IFishSettings extends mongoose.Document{
	waterTemp: number;
	pH: number;
};

var SFishSettings = new mongoose.Schema({
	waterTemp: Number,
	pH: Number
});

export var FishSettings = mongoose.model<IFishSettings>('FishSettings', SFishSettings);

export interface IStandardProfile extends mongoose.Document{
	plantProfile: IPlantSettings[];
	fishProfile: IFishSettings[];
};

var SStandardProfile = new mongoose.Schema({
	plantProfile: [SPlantSettings],
	fishProfile: [SFishSettings]
});

export var StandardProfile = mongoose.model<IStandardProfile>('StandardProfile', SStandardProfile);

