
import json
import unittest


class TestSuiteCR2(unittest.TestCase):
  
 
 #function to test the correct representation of explainability of community smells ose
 def test_case_1_CR_2_ose(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[0]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_ose = smell_data.get("explainability")
        message_example_OSE_explainability= "From the analysis performed on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells OSE, depends on the socio-technical metric PCD, the percentage of core developers. To solve the problem within the team, the number of core developers in the team should be decreased."
        self.assertEqual(explainability_cadocs_ose,message_example_OSE_explainability)


 #function to test the incorrect representation of explainability of community smells ose
 def test_case_1_1_CR_2_ose(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[0]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_ose = smell_data.get("explainability")
        message_example_OSE_explainability=None
        self.assertEqual(explainability_cadocs_ose,message_example_OSE_explainability)
          

 #function to test the correct representation of explainability of community smells bce
 def test_case_2_CR_2_bce(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[1]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_bce = smell_data.get("explainability")
        message_example_BCE_explainability="From the analysis implemented on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells BCE, depends on the socio-technical metric ND,the active relationships between developers within the team. To solve the problem within the team, active relationships between developers should be increased."
        self.assertEqual(explainability_cadocs_bce,message_example_BCE_explainability)
        
 #function to test the incorrect representation of explainability of community smells bce
 def test_case_2_1_CR_2_bce(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[1]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_bce = smell_data.get("explainability")
        message_example_BCE_explainability=None
        self.assertEqual(explainability_cadocs_bce,message_example_BCE_explainability)
        



 #function to test the correct representation of explainability of community smells pde      
 def test_case_3_CR_2_pde(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[2]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_pde = smell_data.get("explainability")
        message_example_PDE_explainability="From the analysis performed on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells PDE, depends on the socio-technical metric NAD, the number of active days of a developer on a project. To solve the problem within the team, developers should work more on the project."
        self.assertEqual(explainability_cadocs_pde,message_example_PDE_explainability)
        
 #function to test the incorrect representation of explainability of community smells pde      
 def test_case_3_1_CR_2_pde(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[2]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_pde = smell_data.get("explainability")
        message_example_PDE_explainability=None
        self.assertEqual(explainability_cadocs_pde,message_example_PDE_explainability)



#function to test the correct representation of explainability of community smells sv     
 def test_case_4_CR_2_sv(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[3]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_sv = smell_data.get("explainability")
        message_example_SV_explainability="From the analysis performed on Explainability using the SHAP framework, we can deduce that the prediction of Community Smells SV, depends on the socio-technical metric ADC, the average number of developers per community. To solve the problem within the team, developers should increase the number of developers within the project."
        self.assertEqual(explainability_cadocs_sv,message_example_SV_explainability)
        

#function to test the incorrect representation of explainability of community smells sv     
 def test_case_4_1_CR_2_sv(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[3]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_sv = smell_data.get("explainability")
        message_example_SV_explainability=None
        self.assertEqual(explainability_cadocs_sv,message_example_SV_explainability)


 #function to test the correct representation of explainability of community smells os      
 def test_case_5_CR_2_os(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[4]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_os= smell_data.get("explainability")
        message_example_OS_explainability="From the analysis performed on Explainability using the SHAP framework, we can deduce that the prediction of Community Smells OS, depends on the socio-technical metric NC, the number of developers in the community. To solve the problem within the team, developers should increase the number of developers within the project."
        self.assertEqual(explainability_cadocs_os,message_example_OS_explainability)
        
#function to test the incorrect representation of explainability of community smells os      
 def test_case_5_1_CR_2_os(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[4]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_os = smell_data.get("explainability")
        message_example_OS_explainability=None
        self.assertEqual(explainability_cadocs_os,message_example_OS_explainability)



#function to test the correct representation of explainability of community smells sd      
 def test_case_6_CR_2_sd(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[5]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_sd = smell_data.get("explainability")
        message_example_SD_explainability="From the analysis implemented on Explainability using the SHAP framework, we can deduce that the prediction of Community Smells SD, depends on the socio-technical metric PCD, the percentage of core developers. To solve the problem within the team the developers should increase the number of core developers within the project."
        self.assertEqual(explainability_cadocs_sd,message_example_SD_explainability)
        
#function to test the incorrect representation of explainability of community smells sd      
 def test_case_6_1_CR_2_sd(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[5]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_sd = smell_data.get("explainability")
        message_example_SD_explainability=None
        self.assertEqual(explainability_cadocs_sd,message_example_SD_explainability)
        



 #function to test the correct representation of explainability of community smells rs       
 def test_case_7_CR_2_rs(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[6]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_rs= smell_data.get("explainability")
        message_example_RS_explainability="From the analysis implemented on Explainability using the SHAP framework, we can deduce that the prediction of Community Smells RS, depends on the socio-technical metric ND, the active relationships between developers within the team. To solve the problem within the team, active relationships between developers should be increased."
        self.assertEqual(explainability_cadocs_rs,message_example_RS_explainability)
        
#function to test the incorrect representation of explainability of community smells rs       
 def test_case_7_1_CR_2_rs(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[6]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_rs = smell_data.get("explainability")
        message_example_RS_explainability=None
        self.assertEqual(explainability_cadocs_rs,message_example_RS_explainability)



 #function to test the correct representation of explainability of community smells tf        
 def test_case_8_CR_2_tf(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[7]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_tf= smell_data.get("explainability")
        message_example_TF_explainability="From the analyses performed on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells TF,depends on the socio-technical metric SCC, the standard deviation of commitments per community. To solve the problem within the team, the commitments of the team developers should be reduced."
        self.assertEqual(explainability_cadocs_tf,message_example_TF_explainability)


#function to test the incorrect representation of explainability of community smells tf        
 def test_case_8_1_CR_2_tf(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[7]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_tf = smell_data.get("explainability")
        message_example_TF_explainability=None
        self.assertEqual(explainability_cadocs_tf,message_example_TF_explainability)


 #function to test the correct representation of explainability of community smells ui       
 def test_case_9_CR_2_ui(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[8]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_ui = smell_data.get("explainability")
        message_example_UI_explainability="From the analysis performed on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells UI, depends on the socio-technical metric NCD, the number of commits per developer in a project. To solve the problem within the team, the number of commits of the team's developers in the project should be increased."
        self.assertEqual(explainability_cadocs_ui,message_example_UI_explainability)
        
 #function to test the incorrect representation of explainability of community smells ui       
 def test_case_9_1_CR_2_ui(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[8]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_ui = smell_data.get("explainability")
        message_example_UI_explainability=None
        self.assertEqual(explainability_cadocs_ui,message_example_UI_explainability)



  #function to test the correct representation of explainability of community smells tc       
 def test_case_10_CR_2_tc(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[9]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_tc = smell_data.get("explainability")
        message_example_TC_explainability="From the analysis implemented on Explainability using the SHAP framework, we can deduce that the prediction of the Community Smells TC, depends on the socio-technical metric NPR, the total number of pull requests. In order to solve the problem within the team, the number of pull requests of the team developers in the project should be increased."
        self.assertEqual(explainability_cadocs_tc,message_example_TC_explainability)
        
  #function to test the incorrect representation of explainability of community smells tc       
 def test_case_10_1_CR_2_tc(self):
     with open('src/community_smells.json') as fp:
        data = json.load(fp)
        smell_data = data[9]  # Assuming the community smell data you want to check is at index 0
        explainability_cadocs_tc = smell_data.get("explainability")
        message_example_TC_explainability=None
        self.assertEqual(explainability_cadocs_tc,message_example_TC_explainability)




if __name__ == '__main__':
    unittest.main()



    