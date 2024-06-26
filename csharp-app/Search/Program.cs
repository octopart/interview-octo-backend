WebApplicationBuilder builder = WebApplication.CreateBuilder(args);

WebApplication app = builder.Build();

string json = File.ReadAllText("Stubs/parts.json");

app.MapGet("/hello", () => json);

app.Run();
