import type { PageLoad } from './$types';
import type { Crossword } from '../@types';
import { env } from '$env/dynamic/public';

import { gql, request } from 'graphql-request';
import dayjs from 'dayjs';

export const load: PageLoad = async () => {
    const data = await request<{ crosswords: Crossword[] }>(env.PUBLIC_HYGRAPH_API_URL as string, gql`
        query($date: DateTime!) {
            crosswords(orderBy: date_DESC, where: {
                date_lte: $date
            }) {
                slug
                title
                author {
                    name
                }
                semester
                date
                width
                height
                data
            }
        }
    `, { date: dayjs().toISOString() });

	return {
        crosswords: data.crosswords,
	};
}
