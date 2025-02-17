# Possible values for parameter 'data' with bulk download method
BULK_DATA = [
    "wind",
    "solar",
    "biomass",
    "hydro",
    "gsgk",
    "combustion",
    "nuclear",
    "gas",
    "storage",
    "electricity_consumer",
    "location",
    "market",
    "grid",
    "balancing_area",
    "permit",
    "deleted_units",
    "retrofit_units",
]

# Possible values for parameter 'data' with API download method
API_DATA = [
    "wind",
    "solar",
    "biomass",
    "hydro",
    "gsgk",
    "combustion",
    "nuclear",
    "storage",
    "location",
    "permit",
]

# Technology related values of parameter 'data'
# Methods like Mastr.to_csv() must separate these from additional tables
TECHNOLOGIES = [
    "wind",
    "solar",
    "biomass",
    "hydro",
    "gsgk",
    "combustion",
    "nuclear",
    "storage",
]

# Data which are not related to a specific technology
ADDITIONAL_TABLES = [
    "balancing_area",
    "electricity_consumer",
    "gas_consumer",
    "gas_producer",
    "gas_storage",
    "gas_storage_extended",
    "grid_connections",
    "grids",
    "locations_extended",
    "market_actors",
    "market_roles",
    "permit",
    "deleted_units",
    "retrofit_units",
]

# Possible data types for API download
API_DATA_TYPES = ["unit_data", "eeg_data", "kwk_data", "permit_data"]

# Possible location types for API download
API_LOCATION_TYPES = [
    "location_elec_generation",
    "location_elec_consumption",
    "location_gas_generation",
    "location_gas_consumption",
]

# Map bulk data to bulk download tables (xml file names)
BULK_INCLUDE_TABLES_MAP = {
    "wind": ["anlageneegwind", "einheitenwind"],
    "solar": ["anlageneegsolar", "einheitensolar"],
    "biomass": ["anlageneegbiomasse", "einheitenbiomasse"],
    "hydro": ["anlageneegwasser", "einheitenwasser"],
    "gsgk": [
        "anlageneeggeothermiegrubengasdruckentspannung",
        "einheitengeothermiegrubengasdruckentspannung",
    ],
    "combustion": ["anlagenkwk", "einheitenverbrennung"],
    "nuclear": ["einheitenkernkraft"],
    "storage": ["anlageneegspeicher", "anlagenstromspeicher", "einheitenstromspeicher"],
    "gas": [
        "anlagengasspeicher",
        "einheitengaserzeuger",
        "einheitengasspeicher",
        "einheitengasverbraucher",
    ],
    "electricity_consumer": ["einheitenstromverbraucher"],
    "location": ["lokationen"],
    "market": ["marktakteure", "marktrollen"],
    "grid": ["netzanschlusspunkte", "netze"],
    "balancing_area": ["bilanzierungsgebiete"],
    "permit": ["einheitengenehmigung"],
    "deleted_units": ["geloeschteunddeaktivierteeinheiten"],
    "retrofit_units": ["ertuechtigungen"],
}

# Map bulk data to database table names, for csv export
BULK_ADDITIONAL_TABLES_CSV_EXPORT_MAP = {
    "gas": [
        "gas_consumer",
        "gas_producer",
        "gas_storage",
        "gas_storage_extended",
    ],
    "electricity_consumer": ["electricity_consumer"],
    "location": ["locations_extended"],
    "market": ["market_actors", "market_roles"],
    "grid": ["grid_connections", "grids"],
    "balancing_area": ["balancing_area"],
    "permit": ["permit"],
    "deleted_units": ["deleted_units"],
    "retrofit_units": ["retrofit_units"],
}

# used to map the parameter options in open-mastr to the exact table class names in orm.py
ORM_MAP = {
    "wind": {
        "unit_data": "WindExtended",
        "eeg_data": "WindEeg",
        "permit_data": "Permit",
    },
    "solar": {
        "unit_data": "SolarExtended",
        "eeg_data": "SolarEeg",
        "permit_data": "Permit",
    },
    "biomass": {
        "unit_data": "BiomassExtended",
        "eeg_data": "BiomassEeg",
        "kwk_data": "Kwk",
        "permit_data": "Permit",
    },
    "combustion": {
        "unit_data": "CombustionExtended",
        "kwk_data": "Kwk",
        "permit_data": "Permit",
    },
    "gsgk": {
        "unit_data": "GsgkExtended",
        "eeg_data": "GsgkEeg",
        "kwk_data": "Kwk",
        "permit_data": "Permit",
    },
    "hydro": {
        "unit_data": "HydroExtended",
        "eeg_data": "HydroEeg",
        "permit_data": "Permit",
    },
    "nuclear": {"unit_data": "NuclearExtended", "permit_data": "Permit"},
    "storage": {
        "unit_data": "StorageExtended",
        "eeg_data": "StorageEeg",
        "permit_data": "Permit",
    },
    "gas_consumer": "GasConsumer",
    "gas_producer": "GasProducer",
    "gas_storage": "GasStorage",
    "gas_storage_extended": "GasStorageExtended",
    "electricity_consumer": "ElectricityConsumer",
    "locations_extended": "LocationExtended",
    "market_actors": "MarketActors",
    "market_roles": "MarketRoles",
    "grid_connections": "GridConnections",
    "grids": "Grids",
    "balancing_area": "BalancingArea",
    "permit": "Permit",
    "deleted_units": "DeletedUnits",
    "retrofit_units": "RetrofitUnits",
}

UNIT_TYPE_MAP = {
    "Windeinheit": "wind",
    "Solareinheit": "solar",
    "Biomasse": "biomass",
    "Wasser": "hydro",
    "Geothermie": "gsgk",
    "Verbrennung": "combustion",
    "Kernenergie": "nuclear",
    "Stromspeichereinheit": "storage",
    "Gasspeichereinheit": "gas_storage",
    "Gasverbrauchseinheit": "gas_consumer",
    "Stromverbrauchseinheit": "electricity_consumer",
    "Gaserzeugungseinheit": "gas_producer",
    "Stromerzeugungslokation": "location_elec_generation",
    "Stromverbrauchslokation": "location_elec_consumption",
    "Gaserzeugungslokation": "location_gas_generation",
    "Gasverbrauchslokation": "location_gas_consumption",
}

TRANSLATIONS = {
    "RegisternummerAusland": "foreignRegisterNumber",
    "PumpbetriebKontinuierlichRegelbar": "continuousControlOfPumpOperation",
    "AuflagenAbschaltungSonstige": "requirementShutdownOther",
    "OrtAnZustelladresse": "cityForDeliveryAddress",
    "RegelzoneNetzanschlusspunkt": "controlZoneNetworkConnectionPoint",
    "EegMastrNummer": "eegMastrNumber",
    "AusschreibungZuschlag": "tenderAward",
    "NameGasspeicher": "gasStorageName",
    "BelieferungVonLetztverbrauchernGas": "supplyToFinalConsumersGas",
    "Registrierungsdatum": "registrationDate",
    "Einheitart": "unitType",
    "BiogasGaserzeugungskapazitaet": "biogasGasProductionCapacity",
    "FernsteuerbarkeitDv": "directMarketerRemoteControl",
    "reason": "reason",
    "GaussKruegerHoch": "gaussKruegerHigh",
    "DatumBeginnVorlaeufigenOderEndgueltigenStilllegung": "startOfTemporaryOrPermanentShutdown",
    "BelieferungHaushaltskundenStrom": "supplyHouseholdCustomersElectricity",
    "GeschlossenesVerteilnetz": "closedDistributionNetwork",
    "DatumWiederaufnahmeBetrieb": "resumptionOfOperationDate",
    "HausnummerAnZustelladresse": "houseNumberForDeliveryAddress",
    "NettonennleistungDeutschland": "netCapacityGermany",
    "DatumBeendigungVorlaeufigenStilllegung": "temporaryShutdownEndDate",
    "KwkMastrNummer": "kwkMastrNumber",
    "NetzMastrNummer": "networkMastrNumber",
    "Nuts2": "nuts2",
    "Yeic": "yeic",
    "request_date": "request_date",
    "Fax_nv": "fax_na",
    "AnzahlStromverbrauchseinheitenGroesser50Mw": "numberPowerConsumptionUnitsGreaterThan50Mw",
    "Registergericht": "commercialRegister",
    "Frist": "deadline",
    "Breitengrad": "latitude",
    "Weic_Na": "weic_na",
    "PilotAnlage": "pilotPlant",
    "MarktakteurNachname": "marketParticipantLastName",
    "MieterstromMeldedatum": "TenantPowerReportingDate",
    "VerhaeltnisReferenzertragErtrag10Jahre_nv": "referenceYieldRatio10YearsYield_na",
    "NameKraftwerksblock": "powerPlantBlockName",
    "Marktrollen": "marketRoles",
    "HauptausrichtungNeigungswinkel": "mainOrientationTiltAngle",
    "Name": "name",
    "Nettoengpassleistung": "netShortCircuitPower",
    "NameWindpark": "windFarmName",
    "Batterietechnologie": "batteryTechnology",
    "VerhaeltnisReferenzertragErtrag10Jahre": "referenceYieldRatio10YearsYield",
    "MieterstromZugeordnet": "TenantPowerAssigned",
    "ClusterOstsee": "clusterBalticSea",
    "BiogasDatumInanspruchnahmeFlexiPraemie": "biogasFlexiPremiumUtilizationDate",
    "UtmEast": "utmEast",
    "Adresszusatz": "addressAdditionalInfo",
    "Bundesland": "state",
    "EinheitSystemstatus": "unitSystemStatus",
    "Datum": "date",
    "WasserrechtAblaufdatum": "waterRightsExpirationDate",
    "ArtDesZuflusses": "typeOfInflow",
    "Technologie": "technology",
    "BiomethanErstmaligerEinsatz_nv": "biomethaneInitialUse_na",
    "Hausnummer": "houseNumber",
    "PostleitzahlAnZustelladresse": "postalCodeForDeliveryAddress",
    "AnlagenkennzifferAnlagenregister": "plantIdentificationNumberRegister",
    "WiederinbetriebnahmeDatum": "recommissioningDate",
    "MinderungStromerzeugung": "reductionElectricityGeneration",
    "Einsatzverantwortlicher": "usageResponsibleEntity",
    "AuflagenAbschaltungSchattenwurf": "requirementShutdownShadowThrow",
    "MaximaleEinspeicherleistung": "maximumInjectionCapacity",
    "Nutzungsbereich": "usageArea",
    "Umsatzsteueridentifikationsnummer_nv": "vatIdentificationNumber_na",
    "Lage": "position",
    "DatenQuelle": "dataSource",
    "AnlagenschluesselEeg": "plantKeyEeg",
    "Laengengrad": "longitude",
    "MarktakteurVorname": "marketParticipantFirstName",
    "HauptwirtdschaftszweigGruppe": "mainEconomicSectorGroup",
    "BiogasLeistungserhoehung": "biogasCapacityIncrease",
    "AnteiligNutzungsberechtigte": "proportionallyAuthorizedUsers",
    "Region": "region",
    "KontaktdatenMarktrolle": "marketRoleContactData",
    "DurchschnittlicherBrennwert": "averageCalorificValue",
    "data_type": "data_type",
    "NebenausrichtungNeigungswinkel": "secondaryOrientationTiltAngle",
    "VerknuepfteEinheit": "linkedUnit",
    "Lokationtyp": "locationType",
    "BestandteilGrenzkraftwerk": "partOfBorderPowerPlant",
    "NameDerTechnischenLokation": "technicalLocationName",
    "GemeinsamerWechselrichterMitSpeicher": "sharedInverterWithStorage",
    "UtmZonenwert": "utmZoneValue",
    "SpeMastrNummer": "speMastrNumber",
    "DatumDownload": "downloadDate",
    "AnlagenbetreiberMastrNummer": "plantOperatorMastrNumber",
    "BilanzierungsgebietNetzanschlusspunkt": "accountingAreaNetworkConnectionPoint",
    "Fax": "fax",
    "Netzbetreiberzuordnungen": "gridOperatorAssignments",
    "NetzreserveAbDatum": "gridReserveFromDate",
    "PrototypAnlage": "prototypePlant",
    "BiogasUmfangLeistungserhoehung": "biogasCapacityIncreaseScope",
    "Kraftwerksnummer_nv": "powerPlantNumber_na",
    "WasserrechtsNummer": "waterRightsNumber",
    "ErtuechtigungIds": "rehabilitationIds",
    "FernsteuerbarkeitDr": "thirdPartyRemoteControl",
    "Einspeisungsart": "feedInType",
    "Umsatzsteueridentifikationsnummer": "vatIdentificationNumber",
    "NetzanschlusspunktMastrNummer": "networkConnectionPointMastrNumber",
    "VerknuepfteErzeugungseinheiten": "linkedGenerationUnits",
    "Marktpartneridentifikationsnummer_nv": "marketPartnerIdentificationNumber_na",
    "Wassertiefe": "waterDepth",
    "WeicDisplayName": "weicDisplayName",
    "eegAnlagenschluessel": "eegPlantKey",
    "Nabenhoehe": "hubHeight",
    "VerhaeltnisErtragsschaetzungReferenzertrag_nv": "yieldEstimationReferenceYieldRatio_na",
    "AuflagenAbschaltungTierschutz": "requirementShutdownAnimalProtection",
    "AnlagenkennzifferAnlagenregister_nv": "plantIdentificationNumberRegister_nv",
    "BiogasDatumLeistungserhoehung": "biogasCapacityIncreaseDate",
    "InAnspruchGenommeneAckerflaeche": "areaOfAgriculturalLandInUse",
    "Aktenzeichen": "fileReference",
    "NetzbetreiberpruefungStatus": "gridOperatorCheckStatus",
    "AnlageBetriebsstatus": "plantOperatingStatus",
    "Gemarkung": "plot",
    "Art": "type",
    "AnschlussAnHoechstOderHochSpannung": "connectionToHighVoltageOrExtraHighVoltage",
    "MaximaleGasbezugsleistung": "maximumGasPurchaseCapacity",
    "InAnspruchGenommeneFlaeche": "areaInUse",
    "BelieferungHaushaltskundenGas": "supplyHouseholdCustomersGas",
    "AnzahlModule": "numberOfModules",
    "Standort": "location",
    "NetzbetreiberMastrNummer": "gridOperatorMastrNumber",
    "ZugeordneteWirkleistungWechselrichter": "assignedReactivePowerInverter",
    "ElektrischeKwkLeistung": "electricalCombinedHeatAndPowerCapacity",
    "Rechtsform": "legalForm",
    "ArtAbschaltbareLast": "typeSwitchableLoad",
    "AnteilBeinflussbareLast": "proportionControllableLoad",
    "NetzanschlusspunktBezeichnung": "networkConnectionPointDescription",
    "Webseite_nv": "website_na",
    "AuflagenAbschaltungSchallimmissionsschutzTagsueber": "requirementShutdownNoiseProtectionDay",
    "BestandsanlageMastrNummer": "inventoryPlantMastrNumber",
    "Gasqualitaet": "gasQuality",
    "Kmu": "smes",
    "download_date": "download_date",
    "NameStromerzeugungseinheit": "powerGenerationUnitName",
    "AnzahlNetzanschlusspunkte": "numberOfNetworkConnectionPoints",
    "BiogasGaserzeugungskapazitaet_nv": "biogasGasProductionCapacity_na",
    "AuflagenAbschaltungSchallimmissionsschutzNachts": "requirementShutdownNoiseProtectionNight",
    "LandAnZustelladresse": "countryForDeliveryAddress",
    "VerhaeltnisErtragsschaetzungReferenzertrag": "yieldEstimationReferenceYieldRatio",
    "VerknuepfteEinheiten": "linkedUnits",
    "InanspruchnahmeZahlungNachEeg": "UseOfPaymentAccordingToEeg",
    "Marktgebiet": "marketArea",
    "Stromgrosshaendler": "electricityWholesaler",
    "AuflagenAbschaltungEiswurf": "requirementShutdownIceThrow",
    "LokationMastrNummer": "locationMastrNumber",
    "RegistrierungsnummerPvMeldeportal_nv": "registrationNumberPvReportingPortal_na",
    "Marktfunktion": "marketFunction",
    "Netzanschlusskapazitaet": "networkConnectionCapacity",
    "Bezeichnung": "designation",
    "FlurFlurstuecknummern": "plotParcelNumbers",
    "MastrNummernKombibetrieb": "mastrNumbersCombinedOperation",
    "SteigerungNettonennleistungKombibetrieb": "increaseInNetCapacityCombinedOperation",
    "ArtDerFlaeche": "typeOfArea",
    "Marktpartneridentifikationsnummer": "marketPartnerIdentificationNumber",
    "Nettonennleistung": "netCapacity",
    "Buergerenergie": "communityEnergy",
    "GaussKruegerRechts": "gaussKruegerRight",
    "ErtuechtigungIstZulassungspflichtig": "upgradeRequiresApproval",
    "Behoerde": "authority",
    "AnlageIstImKombibetrieb": "plantIsInCombinedOperation",
    "WasserrechtAblaufdatum_nv": "waterRightsExpirationDate_na",
    "Leistungsbegrenzung": "powerLimitation",
    "Gasgrosshaendler": "naturalGasWholesaler",
    "NameGasverbrauchsseinheit": "gasConsumptionUnitName",
    "Netzanschlusspunkte": "networkConnectionPoints",
    "Direktvermarktungsunternehmen": "directMarketingCompany",
    "Postleitzahl": "postalCode",
    "Speicherart": "storageType",
    "AcerCode_nv": "acerCode_na",
    "Notstromaggregat": "emergencyGenerator",
    "MaximaleEinspeiseleistung": "maximumFeedInPower",
    "EinheitlicheAusrichtungUndNeigungswinkel": "uniformOrientationAndTiltAngle",
    "Rotordurchmesser": "rotorDiameter",
    "Taetigkeitsende_nv": "activityEndDate_na",
    "Netz": "network",
    "GeplantesInbetriebnahmedatum": "plannedCommissioningDate",
    "Einheittyp": "unitCategory",
    "Land": "country",
    "Hoechstbemessungsleistung": "maximumRatedCapacity",
    "BiomethanErstmaligerEinsatz": "biomethaneInitialUse",
    "InstallierteLeistung": "installedCapacity",
    "AuflageAbschaltungLeistungsbegrenzung": "requirementShutdownPowerLimitation",
    "StrasseNichtGefunden": "streetNotFound",
    "BiogasInanspruchnahmeFlexiPraemie": "biogasFlexiPremiumUtilization",
    "NameStromverbrauchseinheit": "powerConsumptionUnitName",
    "KundenAngeschlossen": "customersConnected",
    "Typenbezeichnung": "modelDesignation",
    "ArtDerWasserkraftanlage": "typeOfHydroPowerPlant",
    "Schwarzstartfaehigkeit": "blackStartCapability",
    "Ort": "place",
    "Leistungserhoehung": "powerIncrease",
    "Energietraeger": "energySource",
    "Inbetriebnahmedatum": "commissioningDate",
    "FernsteuerbarkeitNb": "gridOperatorRemoteControl",
    "Messlokation": "measurementLocation",
    "VerhaeltnisReferenzertragErtrag5Jahre": "referenceYieldRatio5YearsYield",
    "HauptwirtdschaftszweigAbteilung": "mainEconomicSectorDivision",
    "MaximalNutzbaresArbeitsgasvolumen": "maximumUsableWorkingGasVolume",
    "Erzeugungsleistung": "generationCapacity",
    "Hersteller": "manufacturer",
    "AcDcKoppelung": "acDcCoupling",
    "NochInPlanung": "stillInPlanning",
    "DatumEndgueltigeStilllegung": "finalShutdownDate",
    "StrasseAnZustelladresse": "streetForDeliveryAddress",
    "AusschliesslicheVerwendungBiomasse": "exclusiveUseOfBiomass",
    "Frist_nv": "deadline_na",
    "DatumDesBetreiberwechsels": "operatorChangeDate",
    "WeitereBrennstoffe": "otherFuels",
    "EinheitBetriebsstatus": "unitOperationalStatus",
    "Registernummer": "registerNumber",
    "NameKraftwerk": "powerPlantName",
    "Meldedatum": "notificationDate",
    "Einsatzort": "placeOfUse",
    "MarktakteurMastrNummer": "marketParticipantMastrNumber",
    "NameGaserzeugungseinheit": "gasGenerationUnitName",
    "DatumBeginnVoruebergehendeStilllegung": "temporaryShutdownStartDate",
    "Strasse": "street",
    "Ertuechtigungsart": "upgradeType",
    "Gemeinde": "municipality",
    "SicherheitsbereitschaftAbDatum": "securityReadinessFromDate",
    "Email": "email",
    "AcerCode": "acerCode",
    "VerhaeltnisReferenzertragErtrag15Jahre": "referenceYieldRatio15YearsYield",
    "Hauptausrichtung": "mainOrientation",
    "DatumLetzeAktualisierung": "lastUpdateDate",
    "RegistrierungsnummerPvMeldeportal": "RegistrationNumberPvNotificationPortal",
    "AltAnlagenbetreiberMastrNummer": "oldPlantOperatorMastrNumber",
    "DatumBaubeginn": "constructionStartDate",
    "Hauptbrennstoff": "mainFuel",
    "MieterstromErsteZuordnungZuschlag": "TenantPowerFirstAllocationSurcharge",
    "additional_data_id": "additional_data_id",
    "AnzeigeEinerStilllegung": "shutdownNotification",
    "PraequalifiziertGemaessAblav": "prequalifiedAccordingToAblav",
    "EinheitDientDerStromerzeugung": "unitServesElectricityGeneration",
    "Bruttoleistung": "grossCapacity",
    "Marktrolle": "marketRole",
    "ZugeordnenteWirkleistungWechselrichter": "allocatedReactivePowerOfInverter",
    "MaximaleAusspeiseleistung": "maximumWithdrawalPower",
    "Taetigkeitsende": "activityEndDate",
    "Gemeindeschluessel": "municipalityKey",
    "eegZuschlagsnummer": "eegAuctionBidNumber",
    "Biomasseart": "biomassType",
    "AusschliesslicheVerwendungImKombibetrieb": "exclusiveUseInCombinedOperation",
    "Inselbetriebsfaehigkeit": "islandOperationCapability",
    "SonstigeRechtsform": "otherLegalForm",
    "DatumRegistrierungDesBetreiberwechsels": "operatorChangeRegistrationDate",
    "MaximaleAusspeicherleistung": "maximumWithdrawalCapacity",
    "Zuschlagnummer": "grantNumber",
    "UtmNorth": "utmNorth",
    "Weic_nv": "weic_na",
    "BundesnetzagenturBetriebsnummer_nv": "federalNetworkAgencyOperationNumber_na",
    "ClusterNordsee": "clusterNorthSea",
    "Firmenname": "companyName",
    "GenMastrNummer": "genMastrNumber",
    "Seelage": "locationAtSea",
    "Nachtkennzeichen": "nightIdentifier",
    "HausnummerAnZustelladresse_nv": "houseNumberForDeliveryAddress_na",
    "PumpbetriebLeistungsaufnahme": "pumpOperationPowerConsumption",
    "NetzbetreiberpruefungDatum": "gridOperatorCheckDate",
    "AdresszusatzAnZustelladresse": "addressAdditionalInfoForDeliveryAddress",
    "Zuschlagsnummer": "awardNumber",
    "technology": "technology",
    "ThermischeNutzleistung": "thermalUtilizationCapacity",
    "NutzbareSpeicherkapazitaet": "usableStorageCapacity",
    "ArtDerStilllegung": "shutdownType",
    "EegAnlagentyp": "eegPlantType",
    "Sparte": "sector",
    "Personenart": "personType",
    "HauptwirtdschaftszweigAbschnitt": "mainEconomicSectorSection",
    "RegistergerichtAusland": "foreignCommercialRegister",
    "Spannungsebene": "voltageLevel",
    "BilanzierungsgebietNetzanschlusspunktId": "balancingAreaNetworkConnectionPointId",
    "BundesnetzagenturBetriebsnummer": "federalNetworkAgencyOperationNumber",
    "NichtVorhandenInMigriertenEinheiten": "notFoundInMigratedUnits",
    "Ertuechtigung": "rehabilitation",
    "Speichername": "storageName",
    "EinheitMastrNummer": "unitMastrNumber",
    "PraequalifiziertFuerRegelenergie": "prequalifiedForControlEnergy",
    "VerhaeltnisReferenzertragErtrag15Jahre_nv": "referenceYieldRatio15YearsYield_na",
    "ZugeordneteGebotsmenge": "AssignedBidQuantity",
    "Pumpspeichertechnologie": "pumpedStorageTechnology",
    "Id": "id",
    "Webseite": "website",
    "DatumLetzteAktualisierung": "lastUpdateDate",
    "Taetigkeitsbeginn": "activityStartDate",
    "Nebenausrichtung": "secondaryOrientation",
    "location_type": "location_type",
    "HerstellerId": "manufacturerId",
    "Hausnummer_nv": "houseNumber_na",
    "ArtDerFlaecheIds": "typeOfAreaIds",
    "Rotorblattenteisungssystem": "bladeIcingSystem",
    "VerhaeltnisReferenzertragErtrag5Jahre_nv": "referenceYieldRatio5YearsYield_na",
    "BelieferungVonLetztverbrauchernStrom": "supplyToFinalConsumersElectricity",
    "EegInbetriebnahmedatum": "eegCommissioningDate",
    "Telefon": "phone",
    "Landkreis": "district",
    "LetzteAenderung": "lastChange",
    "Weic": "weic",
    "SpeicherMastrNummer": "storageMastrNumber",
    "Kraftwerksnummer": "powerPlantNumber",
    "WeitererHauptbrennstoff": "additionalMainFuel",
    "id": "id",
    "HausnummerNichtGefunden": "houseNumberNotFound",
    "Anlagenbetreiber": "plantOperator",
    "RegistrierungsdatumMarktakteur": "marketParticipantRegistrationDate",
    "MieterstromRegistrierungsdatum": "TenantPowerRegistrationDate",
    "MastrNummer": "mastrNumber",
    "Kuestenentfernung": "distanceToCoast",
    "eegAusschreibungZuschlag": "eegAuctionBidAward",
}
