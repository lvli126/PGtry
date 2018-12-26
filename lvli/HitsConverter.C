#include <fstream>
#include <iomanip>
#include <stdio.h>
{
   gROOT->Reset();
   TFile f("optical.root");

   //TTree *Coincidences = (TTree*)gDirectory->Get("Coincidences");
   TTree *Hits = (TTree*)gDirectory->Get("Hits");
   std::ofstream out("HitsPara.txt");
   //TTree *Singles = (TTree*)gDirectory->Get("Singles");
   //TTree *delay = (TTree*)gDirectory->Get("delay";

//
//Declaration of leaves types - TTree Coincidences
//  
   



   Int_t           runID;
   Int_t           trackID;
   Int_t           photonID;
   Int_t           eventID;
   Int_t           nCompton;
   Int_t           particalID;
   Char_t          proName[30];
   Float_t         globalPosX;
   Float_t         globalPosY;  
   Float_t         globalPosZ;
   Float_t         energy;


   

//   
//Set branch addresses - TTree Hits
// 
   Hits->SetBranchAddress("edep", &energy);
   Hits->SetBranchAddress("trackID", &trackID);
   Hits->SetBranchAddress("runID", &runID);
   Hits->SetBranchAddress("photonID", &photonID);
   Hits->SetBranchAddress("eventID", &eventID);
   Hits->SetBranchAddress("posX", &globalPosX);
   Hits->SetBranchAddress("posY", &globalPosY);
   Hits->SetBranchAddress("posZ", &globalPosZ);
   Hits->SetBranchAddress("nCrystalCompton", &nCompton);
   Hits->SetBranchAddress("processName", &proName);
   Hits->SetBranchAddress("PDGEncoding", &particalID);

   Int_t nentries = Hits->GetEntries();
   Int_t nbytes = 0;

//
// Loop for each event in the TTree Coincidences
//
   out << "runID eventID photonID trackID processName x y z energy nCompton particalID" << std::endl; 
   for (Int_t i=0; i<nentries;i++) {
      nbytes += Hits->GetEntry(i);
      if(out.is_open())
      {
          out<<setw(5)<<runID<<setw(10)<<eventID<<setw(10)<<photonID<<setw(10)<<trackID<<setw(30)<<proName<<setw(20)<<globalPosX<<setw(20)<<globalPosY<<setw(20)<<globalPosZ<<setw(20)<<energy<<setw(5)<<nCompton<<setw(5)<<particalID<<std::endl;
      }
   }
   out.close();
   

}	
