WebApplicationBuilder builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

WebApplication app = builder.Build();

string json = File.ReadAllText("Stubs/parts.json");

app.MapGet("/hello", () => json);

app.MapControllers();

app.Run();
