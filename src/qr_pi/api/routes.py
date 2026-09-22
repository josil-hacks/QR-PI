from fastapi import APIRouter, HTTPException, Query, Response
from qrcode.exceptions import DataOverflowError

from qr_pi.services.qr import generate_qr_svg

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get(
    "/qr.svg",
    response_class=Response,
    responses={
        200: {"content": {"image/svg+xml": {}}},
    },
)
def create_qr_code(
    value: str = Query(
        ...,
        min_length=1,
        max_length=2_000,
        description="Text or URL to encode in the QR code.",
    ),
) -> Response:
    try:
        svg = generate_qr_svg(value)
    except DataOverflowError as error:
        raise HTTPException(
            status_code=422,
            detail="The supplied value is too large to encode as a QR code.",
        ) from error

    return Response(
        content=svg,
        media_type="image/svg+xml",
        headers={
            "Content-Disposition": 'inline; filename="qr-code.svg"',
            "Cache-Control": "no-store",
        },
    )