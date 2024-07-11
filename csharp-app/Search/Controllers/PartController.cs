using Microsoft.AspNetCore.Mvc;

namespace Search.Controllers;

[Route("api/[controller]")]
[ApiController]
public class PartController: ControllerBase
{
    [HttpGet]
    public ActionResult<string> Hello()
    {
        string json = System.IO.File.ReadAllText("Stubs/parts.json");
        return Ok(json);
    }
}
