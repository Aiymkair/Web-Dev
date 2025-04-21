import { Component, OnInit } from '@angular/core';
import { Company } from '../models/company';
import { Vacancy } from '../models/vacancy';
import { CompanyService } from '../services/company.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-list',
  imports: [CommonModule],
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  selectedVacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.loadCompanies();
  }

  loadCompanies(): void {
    this.companyService.getCompanies().subscribe(
      (data: Company[]) => {
        this.companies = data;
      },
      error => {
        console.error('Ошибка при загрузке компаний', error);
      }
    );
  }

  // Метод для загрузки вакансий конкретной компании
  showVacancies(companyId: number): void {
    this.companyService.getCompanyVacancies(companyId).subscribe(
      (data: Vacancy[]) => {
        this.selectedVacancies = data;
      },
      error => {
        console.error('Ошибка при загрузке вакансий', error);
      }
    );
  }
}
