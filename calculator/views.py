from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        calc_type = request.POST.get("calc_type")

        if calc_type == "sgpa":
            credits = request.POST.getlist("credits")
            gradepoints = request.POST.getlist("gradepoints")

            total_credits = 0
            total_points = 0

            for c, gp in zip(credits, gradepoints):
                if c and gp:  # Only process if both values exist
                    c = float(c)
                    gp = float(gp)
                    total_credits += c
                    total_points += c * gp

            if total_credits > 0:
                result = f"SGPA: {round(total_points / total_credits, 2)}"
            else:
                result = "Please enter valid credits and grade points"

        elif calc_type == "cgpa":
            sgpas = request.POST.getlist("sgpas")
            
            valid_sgpas = []
            for sgpa in sgpas:
                if sgpa:
                    valid_sgpas.append(float(sgpa))

            if valid_sgpas:
                result = round(sum(valid_sgpas) / len(valid_sgpas), 2)

        elif calc_type == "percentage":
            marks_obtained = request.POST.get("marks_obtained")
            total_marks = request.POST.get("total_marks")
            if marks_obtained and total_marks:
                marks_obtained = float(marks_obtained)
                total_marks = float(total_marks)
                if total_marks > 0:
                    percentage = (marks_obtained / total_marks) * 100
                    result = f"Percentage: {round(percentage, 2)}%"
                else:
                    result = "Total marks must be greater than 0"

    return render(request, "home.html", {"result": result})

# Create your views here.
