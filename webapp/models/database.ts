import * as mongoose from 'mongoose'

//Benutzer

export interface IUserProfile extends mongoose.Document{//Systemkonfiguration des Benutzer
	foodQuantity: number, //Drehdauer des Futterautomaten
	foodInterval: number, //Anzahl der Fütterungen pro Tag
	exposureTime: number, //Beleuchtungsdauer der Pflanzen
	exposureInterval: number, //Beleuchtungsintervall
	exposureIntensity: number, //Beleuchtungsintensität der Lampen (muss noch geändert werden)
	waterTemp: number, //Wassertemperatur
	autoRegulation: boolean //Automatische Regulierung der Wassertemperatur
}

var SUserProfile = new mongoose.Schema({
	foodQuantity: Number, 
	foodInterval: Number,
	exposureTime: Number, 
	exposureInterval: Number, 
	exposureIntensity: Number,
	waterTemp: Number,
	autoRegulation: boolean
});

export var UserProfile = mongoose.model<IUserProfile>('UserProfile', SUserProfile);

export interface IAccount extends mongoose.Document{
  username: string;
  password: string;
  email: string;
  firstName: string;
  lastName: string;
  systemConfig: IUserProfile[];
}

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
	name: string, //Bezeichnung
	minNumberOfFish: number, //Mindestanzahl von Tieren
	plants: string, //Pflanzen
	planting: string, //Bepflanzung
	origin: string, //Herkunft
	picture: string,
	specialRequirements: string, //Besondere Anforderungen
	food: string,
	waterTemp: string,
	reachableAge: number, //Erreichbares Alter
	pH: number, //pH-Wert
	speciesPool: string //Benötigt Artenbecken (Ja/Nein)
});

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
	name: string //Bezeichnung
	cropDuration: number //Ernte Dauer
	specialRequirements: string //Besondere Anforderungen
});

var SCharacteristics = new mongoose.Schema({
	name: String
	cropDuration: Number
	specialRequirements: String
});

export var Characteristics = mongoose.model<ICharacteristics>('Characteristics', SCharacteristics);

export interface IPlant extends mongoose.Document{
	vegetables: ICharacteristics[],
	fruits: ICharacteristics[],
	herbage: ICharacteristics[] 
});

var SPlant = new mongoose.Schema({
	vegetables:[SCharacteristics],
	fruits: [SCharacteristics],
	herbage: [SCharacteristics] 
});

export var Plant = mongoose.model<IPlant>('Plant', SPlant);

//--------------------------------------------------------------------------------------

//Vordefinierte Profile für Fische und Pflanzen

export interface IPlantSettings extends mongoose.Document{
	exposureTime: number,
	exposureInterval: number,
	exposureIntensity: number //muss noch geändert werden
});

var SPlantSettings = new mongoose.Schema({
	exposureTime: number,
	exposureInterval: number,
	exposureIntensity: number //muss noch geändert werden
});

export var PlantSettings = mongoose.model<IPlantSettings>('PlantSettings', SPlantSettings);

export interface IFishSettings extends mongoose.Document{
	waterTemp: number,
	pH: number
});

var SFishSettings = new mongoose.Schema({
	waterTemp: Number,
	pH: Number
});

export var FishSettings = mongoose.model<IFishSettings>('FishSettings', SFishSettings);

export interface IStandardProfile extends mongoose.Document{
	plantProfile: IPlantSettings[],
	fishProfile: IFishSettings[]
});

var SStandardProfile = new mongoose.Schema({
	plantProfile: [SPlantSettings],
	fishProfile: [SFishSettings]
});

export var StandardProfile = mongoose.model<IStandardProfile>('StandardProfile', SStandardProfile);

