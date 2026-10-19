
class TaxOptimizationEngine:
    def __init__(self, basic_pay: float, hra_received: float, special_allowance: float, digital_investment_vault: dict):
        self.basic = basic_pay
        self.hra_received = hra_received
        self.special_allowance = special_allowance
        self.gross_salary = basic_pay + hra_received + special_allowance
        self.investments = digital_investment_vault

    def calculate_hra_exemption(self, actual_rent_paid: float, city_type: str = "NON_METRO") -> float:
        if actual_rent_paid <= 0:
            return 0.0
        param1 = self.hra_received
        param2 = actual_rent_paid - (0.10 * self.basic)
        metro_multiplier = 0.50 if city_type.upper() == "METRO" else 0.40
        param3 = metro_multiplier * self.basic
        return max(0.0, min(param1, param2, param3))

    def compute_old_regime(self, exempt_hra: float) -> dict:
        standard_deduction = 50000.0
        sec_80c = min(150000.0, self.investments.get("80C", 0.0))
        sec_80d = min(25000.0, self.investments.get("80D", 0.0))
        
        total_deductions = standard_deduction + exempt_hra + sec_80c + sec_80d
        taxable_income = max(0.0, self.gross_salary - total_deductions)
        
        tax = 0.0
        if taxable_income > 1000000:
            tax += (taxable_income - 1000000) * 0.30 + 112500
        elif taxable_income > 500000:
            tax += (taxable_income - 500000) * 0.20 + 12500
        elif taxable_income > 250000:
            tax += (taxable_income - 250000) * 0.05
            
        if taxable_income <= 500000:
            tax = 0.0
            
        return {"taxable_income": taxable_income, "total_tax": tax * 1.04}

    def compute_new_regime(self) -> dict:
        standard_deduction_new = 75000.0
        taxable_income = max(0.0, self.gross_salary - standard_deduction_new)
        
        tax = 0.0
        temp_income = max(0.0, taxable_income - 300000)
        slabs = [(300000, 0.05), (300000, 0.10), (300000, 0.15), (300000, 0.20), (float('inf'), 0.30)]
        
        for slab_limit, rate in slabs:
            if temp_income <= 0:
                break
            taxable_chunk = min(temp_income, slab_limit)
            tax += taxable_chunk * rate
            temp_income -= taxable_chunk

        if taxable_income <= 700000:
            tax = 0.0

        return {"taxable_income": taxable_income, "total_tax": tax * 1.04}

    def optimize(self, actual_rent_paid: float, city_type: str = "NON_METRO") -> dict:
        exempt_hra = self.calculate_hra_exemption(actual_rent_paid, city_type)
        old_res = self.compute_old_regime(exempt_hra)
        new_res = self.compute_new_regime()
        recommended = "NEW_REGIME" if new_res["total_tax"] <= old_res["total_tax"] else "OLD_REGIME"
        potential_savings = abs(old_res["total_tax"] - new_res["total_tax"])
        
        return {
            "gross_annual_salary": self.gross_salary,
            "old_regime_metrics": old_res,
            "new_regime_metrics": new_res,
            "recommended_strategy": recommended,
            "annual_tax_savings": potential_savings,
            "monthly_takehome_boost": round(potential_savings / 12, 2)
        }
