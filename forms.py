from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField

class selectsubdivision(FlaskForm):
    subd = SelectField('SUBDIVISIONS', choices=[('Andaman_Nicobar','ANDAMAN & NICOBAR ISLANDS'),
    	('Arunachal_Pradesh','Arunachal Pradesh'), ('ASSAM_MEGHALAYA','ASSAM & MEGHALAYA'), ('Nagalang_Manipur_Nizoram_Tripura','NAGA MANI MIZO TRIPURA'), 
    	('SUB_HIMALAYAN_WEST_BENGAL_SIKKIM','SUB HIMALAYAN WEST BENGAL & SIKKIM'),('GANGETIC_WEST_BENGAL','GANGETIC WEST BENGAL'),
    	('ORISSA','ORISSA'),('JHARKHAND','JHARKHAND'),('Bihar','Bihar'),('EAST_UTTAR_PRADESH','EAST UTTAR PRADESH'),('WEST_UTTAR_PRADESH','WEST UTTAR PRADESH'),
    	('UTTARAKHAND','UTTARAKHAND'),('HARYANA_DELHI_CHANDIGARH','HARYANA DELHI & CHANDIGARH'),('PUNJAB','PUNJAB'),('HIMACHAL_PRADESH','HIMACHAL PRADESH'),
    	('JAMMU_KASHMIR','JAMMU & KASHMIR'),('WEST_RAJASTHAN','WEST RAJASTHAN'),('EAST_RAJASTHAN','EAST RAJASTHAN'),('WEST_MADHYA_PRADESH','WEST MADHYA PRADESH'),
    	('EAST_MADHYA_PRADESH','EAST MADHYA PRADESH'),('GUJARAT_REGION','GUJARAT REGION'),('SAURASHTRA_KUTCH','SAURASHTRA & KUTCH'),('KONKAN_GOA','KONKAN & GOA'),
    	('MADHYA_MAHARASHTRA','MADHYA MAHARASHTRA'),('MATATHWADA','MATATHWADA'),('VIDARBHA','VIDARBHA'),('CHHATTISGARH','CHHATTISGARH'),('COASTAL_ANDHRA_PRADESH','COASTAL ANDHRA PRADESH'),
    	('TELANGANA','TELANGANA'),('RAYALSEEMA','RAYALSEEMA'),('TAMIL_NADU','TAMIL NADU'),('COASTAL_KARNATAKA','COASTAL KARNATAKA'),('NORTH_INTERIOR_KARNATAKA','NORTH INTERIOR KARNATAKA'),
    	('SOUTH_INTERIOR_KARNATAKA','SOUTH INTERIOR KARNATAKA'),('KERALA','KERALA'),('LAKSHADWEEP','LAKSHADWEEP')])
    submit = SubmitField('Submit')


class selectsubdivisionp(FlaskForm):
    subdp = SelectField('SUBDIVISIONS', choices=[('A_N','ANDAMAN & NICOBAR ISLANDS'),
        ('A_P','Arunachal Pradesh'), ('A_M','ASSAM & MEGHALAYA'), ('N_M_N_T','NAGA MANI MIZO TRIPURA'), 
        ('S_H_W_B_S','SUB HIMALAYAN WEST BENGAL & SIKKIM'),('G_W_B','GANGETIC WEST BENGAL'),
        ('O','ORISSA'),('J','JHARKHAND'),('B','Bihar'),('E_U_P','EAST UTTAR PRADESH'),('W_U_P','WEST UTTAR PRADESH'),
        ('U','UTTARAKHAND'),('H_D_C','HARYANA DELHI & CHANDIGARH'),('P','PUNJAB'),('H_P','HIMACHAL PRADESH'),
        ('J_K','JAMMU & KASHMIR'),('W_R','WEST RAJASTHAN'),('E_R','EAST RAJASTHAN'),('W_M_P','WEST MADHYA PRADESH'),
        ('E_M_P','EAST MADHYA PRADESH'),('G_R','GUJARAT REGION'),('S_K','SAURASHTRA & KUTCH'),('K_G','KONKAN & GOA'),
        ('M_M','MADHYA MAHARASHTRA'),('M','MATATHWADA'),('V','VIDARBHA'),('C','CHHATTISGARH'),('C_A_P','COASTAL ANDHRA PRADESH'),
        ('T','TELANGANA'),('R','RAYALSEEMA'),('T_N','TAMIL NADU'),('C_K','COASTAL KARNATAKA'),('N_I_K','NORTH INTERIOR KARNATAKA'),
        ('S_I_K','SOUTH INTERIOR KARNATAKA'),('K','KERALA'),('L','LAKSHADWEEP')])
    submit = SubmitField('Submit')