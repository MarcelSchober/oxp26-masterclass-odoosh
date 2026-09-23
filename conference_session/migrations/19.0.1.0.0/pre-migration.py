def migrate(cr, version):
    cr.execute("""
        ALTER TABLE conference_session
        ADD COLUMN presenter_id integer
    """)

  cr.execute("""
        UPDATE conference_session AS session
        SET presenter_id = partner.id
        FROM res_partner AS partner
        WHERE partner.name = session.speaker
    """)

    cr.execute("""
        ALTER TABLE conference_session
        ALTER COLUMN duration TYPE double precision
    """)
