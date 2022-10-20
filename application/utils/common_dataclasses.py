from attrs import define, asdict

@define
class BasicResponse:
    message: str
    status: bool

    @property
    def response(self):
        return asdict(self)
